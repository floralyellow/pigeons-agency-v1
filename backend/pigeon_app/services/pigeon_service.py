import random
from datetime import timedelta

from django.db import transaction
from django.utils import timezone

from ..exceptions.custom_exceptions import ServiceException
from ..models import Pigeon, TR_Expedition, TR_Lvl_info, TR_Pigeon
from ..models.pigeon import PigeonSerializer


def get_global_pigeon_info(user):
    query = "select 1 as id, coalesce(sum(droppings_minute),0) as droppings_minute ,count(*) as nb_pigeons from pigeon_app_pigeon pap where player_id = %s and is_open = true and is_sold = false;"
    res = Pigeon.objects.raw(query, [user.id])[0]
    return res.nb_pigeons, res.droppings_minute


def create_pigeon(user, expedition_lvl, expedition_type):
    """
    create new pigeon
    """

    with transaction.atomic():
        expedition_lvl = int(expedition_lvl)
        expedition_type = int(expedition_type)

        player = user.player
        if player.lvl < expedition_lvl:
            raise ServiceException("Error: Invalid lvl !")

        pigeon_type = random.randint(1, 3)
        # expedition type input gives slighlty more chances to get wanted pigeon if we did not get it (1/3 to 1/2)
        if expedition_type < 4 and pigeon_type != expedition_type:
            chance_to_change_type = random.randint(1, 4)
            if chance_to_change_type == 4:  # 1 chance / 4
                pigeon_type = expedition_type

        expedition = TR_Expedition.objects.filter(lvl=expedition_lvl)[0]

        lvl_info = TR_Lvl_info.objects.filter(lvl=player.lvl)[0]
        nb_pigeons = Pigeon.objects.filter(player_id=user.id, is_sold=False).count()

        if nb_pigeons >= lvl_info.max_pigeons:
            raise ServiceException("Error: too many pigeons !")
        if player.seeds < expedition.seeds:
            raise ServiceException("Error: Not enough seeds !")

        player.seeds = player.seeds - expedition.seeds
        player.save()

        luck_value = random.randint(1, 100)

        add_pigeon(user.id, expedition, pigeon_type, luck_value)

        expeditions = Pigeon.objects.filter(player_id=user.id, is_open=False)

    return list(expeditions.values())


def add_pigeon(user_id, expedition, pigeon_type, luck_value):
    """
    not directly an endpoint
    used for create_pigeon endpoint
    """
    p = TR_Pigeon.objects.filter(lvl_expedition=expedition.lvl, pigeon_type=pigeon_type)[0]

    phys_atk = round(luck_value / 100 * (p.max_phys_atk - p.min_phys_atk)) + p.min_phys_atk
    magic_atk = round(luck_value / 100 * (p.max_magic_atk - p.min_magic_atk)) + p.min_magic_atk
    shield = round(luck_value / 100 * (p.max_shield - p.min_shield)) + p.min_shield
    drop_min = (
        round(luck_value / 100 * (expedition.max_drop_minute - expedition.min_drop_minute))
        + expedition.min_drop_minute
    )
    feathers = (
        round(luck_value / 100 * (expedition.max_feathers - expedition.min_feathers))
        + expedition.min_feathers
    )

    pigeon_name = p.name[0]  # only 1 per type/lvl now
    pigeon_src = p.src[0]

    # Small chance to get a custom skin for high luck pigeons
    if expedition.lvl >= 5 and luck_value >= 98:  # high legendary

        if luck_value == 98:
            pigeon_name = "Pandgeon"
            pigeon_src = "pandgeon.png"
        elif luck_value > 98:
            SPECIAL_PIGEONS_MAPPING = {
                1: {"name": "Drageon", "src": "drageon.png"},
                2: {"name": "Firegeon", "src": "firegeon.png"},
                3: {"name": "Squelegeon", "src": "squelegeon.png"},
            }
            pigeon_name = SPECIAL_PIGEONS_MAPPING[p.pigeon_type]["name"]
            pigeon_src = SPECIAL_PIGEONS_MAPPING[p.pigeon_type]["src"]

    creation_time = timezone.now()
    active_time = creation_time + timedelta(0, expedition.duration)

    new_pigeon = Pigeon(
        player_id=user_id,
        pigeon_type=p.pigeon_type,
        name=pigeon_name,
        src=pigeon_src,
        pigeon_id=p.pigeon_id,
        luck=luck_value,
        lvl=expedition.lvl,
        phys_atk=phys_atk,
        magic_atk=magic_atk,
        shield=shield,
        droppings_minute=drop_min,
        feathers=feathers,
        creation_time=creation_time,
        active_time=active_time,
    )
    new_pigeon.save()


def set_in_team_A(user, pigeon_id):

    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(
            player_id=user.id, is_sold=False, is_open=True
        )

        if int(pigeon_id) not in pigeons.values_list("id", flat=True):
            raise ServiceException("Error: wrong id !")

        pigeon_to_update = pigeons.filter(id=pigeon_id)[0]

        pigeon_to_update.is_in_team_A = not pigeon_to_update.is_in_team_A

        nb_in_team = pigeons.filter(is_in_team_A=True).count()

        if nb_in_team > 5:
            raise ServiceException("Error: Too many in team !")

        pigeon_to_update.save()

    return PigeonSerializer(pigeon_to_update).data


def set_in_team_B(user, pigeon_id):

    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(
            player_id=user.id, is_sold=False, is_open=True
        )

        if int(pigeon_id) not in pigeons.values_list("id", flat=True):
            raise ServiceException("Error: wrong id !")

        pigeon_to_update = pigeons.filter(id=pigeon_id)[0]

        pigeon_to_update.is_in_team_B = not pigeon_to_update.is_in_team_B

        nb_in_team = pigeons.filter(is_in_team_B=True).count()

        if nb_in_team > 5:
            raise ServiceException("Error:  Too many in team !")

        pigeon_to_update.save()

    return PigeonSerializer(pigeon_to_update).data


def activate_pigeon(user, pigeon_id):
    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(
            player_id=user.id, is_sold=False, is_open=False
        )

        if int(pigeon_id) not in pigeons.values_list("id", flat=True):
            raise ServiceException("Error: wrong id !")

        pigeon_to_activate = pigeons.filter(id=pigeon_id)[0]

        if timezone.now() < pigeon_to_activate.active_time:
            raise ServiceException("Error: pigeon not yet active !")

        pigeon_to_activate.is_open = True

        pigeon_to_activate.save()
    return PigeonSerializer(pigeon_to_activate).data


def sell_pigeon(user, pigeon_id):
    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(
            player_id=user.id, is_sold=False, is_open=True
        )

        if int(pigeon_id) not in pigeons.values_list("id", flat=True):
            raise ServiceException("Error: wrong id !")

        max_feathers = TR_Lvl_info.objects.get(lvl=user.player.lvl).max_feathers

        pigeon_to_sell = pigeons.filter(id=pigeon_id)[0]

        feathers_to_apply = user.player.feathers + pigeon_to_sell.feathers

        user.player.feathers = min(feathers_to_apply, max_feathers)

        pigeon_to_sell.is_sold = True
        pigeon_to_sell.is_in_team_A = False
        pigeon_to_sell.is_in_team_B = False

        pigeon_to_sell.save()
        user.player.save()
    return PigeonSerializer(pigeon_to_sell).data
