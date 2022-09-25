from django.http import JsonResponse
from django.contrib.auth.models import User
import logging
from django.utils import timezone
from ..models import TR_Pigeon
from ..models import TR_Lvl_info
from ..models import TR_Expedition
from datetime import datetime,timedelta
from ..models import Player, Pigeon, Adventure,PvePigeon
import random
from django.db import transaction


def get_adventure(user):

    with transaction.atomic():
        last_adventure = Adventure.objects.filter(player_id=user.id, lvl=user.player.lvl).order_by('-encounter').first()

        if last_adventure is None or last_adventure.is_success:
            adventure = create_adventure(user, last_adventure)
        else:
            adventure = last_adventure

    return adventure


def create_adventure(user, last_adventure):
    """
    create new adventure
    """
    lvl_info = TR_Lvl_info.objects.get(lvl=user.player.lvl)

    new_adventure = Adventure(
        player_id=user.id, 
        lvl = user.player.lvl,
        encounter = last_adventure.encounter + 1 if last_adventure else 1,
        nb_tries = 0,
        is_success = False,
        reward_droppings = int(lvl_info.max_droppings * 0.15)
        )
    new_adventure.save()

    return new_adventure


def get_adventure_pigeons(lvl, encounter):
    pve_pigeons = None
    if encounter == 1:
        p1 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 1, luck=20)
        p2 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 1, luck=20)
        p3 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 2, luck=20)
        p4 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 2, luck=20)
        p5 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 3, luck=20)
        pve_pigeons = p1.union(p2,p3,p4,p5, all=True)
    elif encounter == 2:
        p1 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 1, luck=20)
        p2 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 1, luck=20)
        p3 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 3, luck=20)
        p4 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 3, luck=20)
        p5 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 2, luck=20)
        pve_pigeons = p1.union(p2,p3,p4,p5, all=True)
    elif encounter >= 3:
        p1 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 1, luck=20)
        p2 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 1, luck=40)
        p3 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 2, luck=20)
        p4 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 2, luck=40)
        p5 = PvePigeon.objects.filter(lvl = lvl, pigeon_type = 3, luck=40)
        pve_pigeons = p1.union(p2,p3,p4,p5, all=True)

    return pve_pigeons
