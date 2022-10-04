import random
from datetime import datetime, timedelta, timezone
from typing import Any, Tuple

from django.db import transaction
from pigeon_app.models.attack import AttackSerializer

from ..exceptions.custom_exceptions import ServiceException
from ..models import Attack, AttackPigeon, Pigeon, Player


def _handle_attack_logic(
    pigeons: Any, current_attack: Attack, is_attacker: bool
) -> Tuple[int, int, int]:
    """
    Handle main attack loop

    Args:
        pigeons: queryset of pigeons
        current_attack: used for reference
        is_attacker:

    Returns:
        Totals of physical & magical attack, + opposing team shield blocs
    """
    VARIANCE = 15
    # init
    total_phys = 0
    total_magic = 0
    total_shield_blocs_opposing_team = 0
    for p in pigeons:
        bonus_phys_atk = round(random.randint(-VARIANCE, VARIANCE) * p.phys_atk / 100)
        bonus_magic_atk = round(random.randint(-VARIANCE, VARIANCE) * p.magic_atk / 100)

        if p.phys_atk > 0:
            total_phys += p.phys_atk + bonus_phys_atk
            total_shield_blocs_opposing_team += 1

        total_magic += p.magic_atk + bonus_magic_atk

        attack_pigeon = AttackPigeon(
            attack=current_attack,
            pigeon=p,
            is_attacker=is_attacker,
            phys_atk_bonus=bonus_phys_atk,
            magic_atk_bonus=bonus_magic_atk,
        )
        attack_pigeon.save()

    return total_phys, total_magic, total_shield_blocs_opposing_team


def attack_player(user, target_id, attack_team):

    SECONDS_NEXT_ATTACK = 2 * 60  # 2 minutes

    with transaction.atomic():
        target = Player.objects.filter(id=target_id)

        if len(target) != 1 or target_id == user.id:
            raise ServiceException("Error: Invalid id")

        if target_id == user.player.last_attacked:
            raise ServiceException("Error: Cant attack same player twice !")

        if user.player.time_last_attack + timedelta(seconds=SECONDS_NEXT_ATTACK) > datetime.now(
            timezone.utc
        ):
            raise ServiceException("Error: Cant attack yet !")

        if attack_team == "A":
            attacking_pigeons = Pigeon.objects.filter(player_id=user.id, is_in_team_A=True)
        elif attack_team == "B":
            attacking_pigeons = Pigeon.objects.filter(player_id=user.id, is_in_team_B=True)

        defender = target[0]

        defend_team = defender.defense_team
        if defend_team == "A":
            defending_pigeons = Pigeon.objects.filter(player_id=target_id, is_in_team_A=True)
        elif defend_team == "B":
            defending_pigeons = Pigeon.objects.filter(player_id=target_id, is_in_team_B=True)

        # sum shields needed before loop
        sum_shield_value_atk = sum([i.shield for i in attacking_pigeons])
        sum_shield_value_def = sum([i.shield for i in defending_pigeons])

        current_attack = Attack(attacker=user.player, defender=defender)
        current_attack.save()

        # scores for attackers
        total_phys_atk, total_magic_atk, total_blocs_def = _handle_attack_logic(
            attacking_pigeons, current_attack, True
        )

        # scores for defenders
        total_phys_def, total_magic_def, total_blocs_atk = _handle_attack_logic(
            defending_pigeons, current_attack, False
        )

        total_attacker = (
            total_phys_atk
            + total_magic_atk
            - min((sum_shield_value_def * total_blocs_def), total_phys_atk)
        )
        total_defender = (
            total_phys_def
            + total_magic_def
            - min((sum_shield_value_atk * total_blocs_atk), total_phys_def)
        )

        winner_id = user.id if total_attacker > total_defender else target_id

        # TODO stolen droppings

        # TODO militaryscore

        # TODO timetonextattack & last attack id

        # TODO protecteduntil (with model)

        current_attack.winner_id = winner_id
        current_attack.atk_tot_score = total_attacker
        current_attack.atk_tot_phys = total_phys_atk
        current_attack.atk_tot_magic = total_magic_atk
        current_attack.atk_shield_value = sum_shield_value_atk
        current_attack.atk_shield_blocs = total_blocs_atk

        current_attack.def_tot_score = total_defender
        current_attack.def_tot_phys = total_phys_def
        current_attack.def_tot_magic = total_magic_def
        current_attack.def_shield_value = sum_shield_value_def
        current_attack.def_shield_blocs = total_blocs_def

        current_attack.stolen_droppings = 0
        current_attack.atk_old_military_score = 0
        current_attack.atk_new_military_score = 0
        current_attack.def_old_military_score = 0
        current_attack.def_new_military_score = 0
        current_attack.save()

        fighting_pigeons = AttackPigeon.objects.filter(attack=current_attack)

    return AttackSerializer(current_attack).data, fighting_pigeons
