import random
from typing import Any, Tuple

from django.db import transaction

from ..models import Adventure, AdventureAttack, Pigeon, PvePigeon, TR_Lvl_info


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
        reward_droppings=int(lvl_info.max_droppings * 0.15),
    )
    new_adventure.save()

    return new_adventure


def get_adventure_pigeons(lvl, encounter):
    pve_pigeons = None
    if encounter == 1:
        p1 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=1, luck=20)
        p2 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=1, luck=20)
        p3 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=2, luck=20)
        p4 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=2, luck=20)
        p5 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=3, luck=20)
        pve_pigeons = p1.union(p2, p3, p4, p5, all=True)
    elif encounter == 2:
        p1 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=1, luck=20)
        p2 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=1, luck=20)
        p3 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=3, luck=20)
        p4 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=3, luck=20)
        p5 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=2, luck=20)
        pve_pigeons = p1.union(p2, p3, p4, p5, all=True)
    elif encounter >= 3:
        p1 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=1, luck=20)
        p2 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=1, luck=40)
        p3 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=2, luck=20)
        p4 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=2, luck=40)
        p5 = PvePigeon.objects.filter(lvl=lvl, pigeon_type=3, luck=40)
        pve_pigeons = p1.union(p2, p3, p4, p5, all=True)

    return pve_pigeons


def _handle_adventure_attack_logic(pigeons: Any) -> Tuple[int, int, int]:
    """
    Handle main attack loop

    Args:
        pigeons: queryset of pigeons

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

    return total_phys, total_magic, total_shield_blocs_opposing_team


def try_adventure(user, attack_team: str):
    if attack_team == "A":
        attacking_pigeons = Pigeon.objects.filter(player_id=user.id, is_in_team_A=True)
    elif attack_team == "B":
        attacking_pigeons = Pigeon.objects.filter(player_id=user.id, is_in_team_B=True)

    current_adventure = get_adventure(user)

    defending_pigeons = get_adventure_pigeons(current_adventure.lvl, current_adventure.encounter)

    # sum shields needed before loop
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

    total_attacker = total_phys_atk + total_magic_atk - (sum_shield_value_def * total_blocs_def)
    total_defender = total_phys_def + total_magic_def - (sum_shield_value_atk * total_blocs_atk)

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

    return adventure_attack
