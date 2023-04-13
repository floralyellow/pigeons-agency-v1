import random
from datetime import datetime, timezone
from typing import Any, Tuple

from django.db import transaction

from ..models import Adventure, AdventureAttack, PvePigeon, TR_Lvl_info
from ..utils.commons import (
    ADVENTURE_RATIO_REWARDS,
    ATTACK_VARIANCE,
    LOST_DROPPINGS_ADVENTURE_RATIO,
    get_pigeon_team,
    get_total_score,
)
from ..utils.pve_pigeons import pve_pigeons_list


def get_adventure(user):

    with transaction.atomic():
        last_adventure = (
            Adventure.objects.filter(player_id=user.id, lvl=user.player.lvl)
            .order_by("-encounter")
            .first()
        )

        if last_adventure is None or last_adventure.is_success:
            adventure = _create_adventure(user, last_adventure)
        else:
            adventure = last_adventure

    return adventure


def _create_adventure(user, last_adventure):
    """
    create new adventure
    """
    lvl_info = TR_Lvl_info.objects.get(lvl=user.player.lvl)

    new_adventure = Adventure(
        player_id=user.id,
        lvl=user.player.lvl,
        encounter=last_adventure.encounter + 1 if last_adventure else 1,
        nb_tries=0,
        is_success=False,
        reward_droppings=int(lvl_info.max_droppings * ADVENTURE_RATIO_REWARDS),
    )
    new_adventure.save()

    return new_adventure


def get_adventure_pigeons(lvl, encounter):
    MAX_ENCOUNTER_LEVEL = 13
    pve_pigeons = None
    encounter_level = min(encounter, MAX_ENCOUNTER_LEVEL)

    pve_pigeons_stats = pve_pigeons_list.get(encounter_level)

    pigeon_qs_list = []
    for pigeon_stat in pve_pigeons_stats:
        pigeon_qs = PvePigeon.objects.filter(
            lvl=lvl, pigeon_type=pigeon_stat["pigeon_type"], luck=pigeon_stat["luck"]
        )
        pigeon_qs_list.append(pigeon_qs)

    pve_pigeons = pigeon_qs_list[0].union(*pigeon_qs_list[1:], all=True)

    return pve_pigeons


def _handle_adventure_attack_logic(pigeons: Any) -> Tuple[int, int, int]:
    """
    Handle main attack loop

    Args:
        pigeons: queryset of pigeons

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

    return total_phys, total_magic, total_shield_blocs_opposing_team


def try_adventure(user, attack_team: str):
    with transaction.atomic():
        attacking_pigeons = get_pigeon_team(user.id, attack_team)

        current_adventure = get_adventure(user)

        defending_pigeons = get_adventure_pigeons(
            current_adventure.lvl, current_adventure.encounter
        )

        # sum shields
        sum_shield_value_atk = sum([i.shield for i in attacking_pigeons])
        sum_shield_value_def = sum([i.shield for i in defending_pigeons])

        # scores for attackers (user)
        total_phys_atk, total_magic_atk, total_blocs_def = _handle_adventure_attack_logic(
            attacking_pigeons
        )

        # scores for defenders (adventure)
        total_phys_def, total_magic_def, total_blocs_atk = _handle_adventure_attack_logic(
            defending_pigeons
        )

        total_attacker = get_total_score(
            total_phys_atk, total_magic_atk, sum_shield_value_def, total_blocs_def
        )
        total_defender = get_total_score(
            total_phys_def, total_magic_def, sum_shield_value_atk, total_blocs_atk
        )

        is_victory: bool = total_attacker > total_defender

        adventure_attack = AdventureAttack(
            attacker=user.player,
            adventure=current_adventure,
            is_victory=is_victory,
            atk_tot_score=total_attacker,
            atk_tot_phys=total_phys_atk,
            atk_tot_magic=total_magic_atk,
            atk_shield_value=sum_shield_value_atk,
            atk_shield_blocs=total_blocs_atk,
            def_tot_score=total_defender,
            def_tot_phys=total_phys_def,
            def_tot_magic=total_magic_def,
            def_shield_value=sum_shield_value_def,
            def_shield_blocs=total_blocs_def,
        )

        adventure_attack.save()

        current_adventure.nb_tries += 1
        max_droppings = TR_Lvl_info.objects.get(lvl=user.player.lvl).max_droppings

        if is_victory:
            current_adventure.is_success = True
            current_adventure.completed_at = datetime.now(timezone.utc)
            user.player.droppings = min(
                user.player.droppings + current_adventure.reward_droppings, max_droppings
            )
        else:
            user.player.droppings = max(
                user.player.droppings
                - int(current_adventure.reward_droppings * LOST_DROPPINGS_ADVENTURE_RATIO),
                0,
            )
        user.player.save()
        current_adventure.save()

        return adventure_attack, current_adventure
