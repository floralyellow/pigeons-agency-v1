import random
from datetime import datetime, timedelta, timezone
from typing import Any, Tuple

from django.contrib.auth.models import User
from django.db import transaction

from ..exceptions.custom_exceptions import ServiceException
from ..models import Attack, AttackPigeon
from ..models.attack import AttackSerializer
from ..models.player import UserSerializer
from ..models.tr_lvl_info import TR_Lvl_info
from ..services import update_service
from ..utils.commons import (
    ATTACK_VARIANCE,
    DELAY_SECONDS_BETWEEN_ATTACKS,
    PROTECTED_UNTIL_MINUTES,
    get_pigeon_team,
    get_total_score,
)


def _calculate_won_military_score(difference_scores: int, max_value: int, soft_coef: int) -> int:
    return max(min(max_value - round(difference_scores / soft_coef), max_value), 0)


def _get_won_military_scores(
    attacker_is_winner: bool, atk_military_score: int, def_military_score: int
) -> Tuple[int, int]:
    diff_scores = atk_military_score - def_military_score
    if attacker_is_winner:
        attacker_won_score = +(_calculate_won_military_score(diff_scores, 7, 5))
        defender_won_score = -(_calculate_won_military_score(diff_scores, 6, 5))
    else:
        attacker_won_score = -(_calculate_won_military_score(-diff_scores, 5, 6))
        defender_won_score = +(_calculate_won_military_score(-diff_scores, 6, 6))
    return attacker_won_score, defender_won_score


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
    # init
    total_phys = 0
    total_magic = 0
    total_shield_blocs_opposing_team = 0
    for p in pigeons:
        bonus_phys_atk = round(random.randint(-ATTACK_VARIANCE, ATTACK_VARIANCE) * p.phys_atk / 100)
        bonus_magic_atk = round(
            random.randint(-ATTACK_VARIANCE, ATTACK_VARIANCE) * p.magic_atk / 100
        )

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

    with transaction.atomic():
        user_target = User.objects.filter(id=target_id)

        if len(user_target) != 1 or target_id == user.id:
            raise ServiceException("Error: Invalid id")

        if target_id == user.player.last_attacked:
            raise ServiceException("Error: Cant attack same player twice !")

        attack_datetime = datetime.now(timezone.utc)

        if (
            user.player.time_last_attack + timedelta(seconds=DELAY_SECONDS_BETWEEN_ATTACKS)
            > attack_datetime
        ):
            raise ServiceException("Error: Cant attack yet !")

        defender = user_target[0].player

        if defender.protected_until > attack_datetime:
            raise ServiceException("Error: Cant attack this user yet !")

        attacking_pigeons = get_pigeon_team(user.id, attack_team)

        defend_team = defender.defense_team
        defending_pigeons = get_pigeon_team(target_id, defend_team)

        # sum shield
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

        total_attacker = get_total_score(
            total_phys_atk, total_magic_atk, sum_shield_value_def, total_blocs_def
        )
        total_defender = get_total_score(
            total_phys_def, total_magic_def, sum_shield_value_atk, total_blocs_atk
        )

        winner_id = user.id if total_attacker > total_defender else target_id
        attacker_is_winner = winner_id == user.id

        attacker_won_score, defender_won_score = _get_won_military_scores(
            attacker_is_winner, user.player.military_score, defender.military_score
        )
        # rewards
        update_service.update_user_values(defender.user)

        atk_max_droppings = TR_Lvl_info.objects.get(lvl=user.player.lvl).max_droppings
        def_max_droppings = TR_Lvl_info.objects.get(lvl=defender.lvl).max_droppings

        current_attack.atk_old_military_score = user.player.military_score
        current_attack.def_old_military_score = defender.military_score

        if attacker_is_winner:
            stolen_droppings = int(
                min((def_max_droppings + defender.droppings) / 2 * 0.2, defender.droppings)
            )
        else:
            stolen_droppings = int(
                -min((atk_max_droppings + user.player.droppings) / 2 * 0.2, user.player.droppings)
            )

        # update values for both players

        user.player.military_score = max(user.player.military_score + attacker_won_score, 0)
        defender.military_score = max(defender.military_score + defender_won_score, 0)

        user.player.droppings = max(
            min(user.player.droppings + stolen_droppings, atk_max_droppings), 0
        )
        defender.droppings = max(min(defender.droppings - stolen_droppings, def_max_droppings), 0)

        user.player.time_last_attack = attack_datetime
        user.player.last_attacked = target_id

        user.player.protected_until = attack_datetime
        defender.protected_until = attack_datetime + timedelta(minutes=PROTECTED_UNTIL_MINUTES)

        defender.nb_notifs += 1

        user.player.save()
        defender.save()

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

        current_attack.stolen_droppings = stolen_droppings
        current_attack.atk_new_military_score = user.player.military_score
        current_attack.def_new_military_score = defender.military_score
        current_attack.save()

    return (
        AttackSerializer(current_attack).data,
        attacking_pigeons,
        defending_pigeons,
        user_target[0],
    )


def get_ordered_attack_list(user):
    """
    return list of users in order :
    - difference in lvl
    - lvl desc
    - difference in military score
    - military score desc
    """
    users = UserSerializer(
        User.objects.select_related("player")
        .extra(
            select={"offset_military": "abs(pigeon_app_player.military_score - %s)"},
            select_params=(user.player.military_score,),
        )
        .extra(
            select={"offset_lvl": "abs(pigeon_app_player.lvl - %s)"},
            select_params=(user.player.lvl,),
        )
        .extra(
            select={"id_diff": "abs(pigeon_app_player.id - %s)"}, select_params=(user.player.id,)
        )
        .order_by(
            "offset_lvl", "-player__lvl", "offset_military", "-player__military_score", "id_diff"
        ),
        many=True,
    ).data

    return users
