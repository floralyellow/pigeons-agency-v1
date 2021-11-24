from pigeon_app.models.player import UserSerializer
from pigeon_app.models.player import PlayerSerializer
from pigeon_app.models.pigeon import PigeonSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from ..models import Player
from ..models import Pigeon
import logging
from django.core import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone
from ..models import TR_Pigeon
from ..models import TR_Lvl_info
from ..models import TR_Expedition
from datetime import datetime,timedelta
import random
from django.db import transaction

def get_global_pigeon_info(user):
    query = 'select 1 as id, coalesce(sum(droppings_minute),0) as droppings_minute ,count(*) as nb_pigeons from pigeon_app_pigeon pap where player_id = %s and is_open = true and is_sold = false;'
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
            return 'Invalid lvl'
        
        pigeon_type = random.randint(1,3)
        # expedition type input gives slighlty more chances to get wanted pigeon if we did not get it (1/3 to 1/2)
        if expedition_type < 4 and pigeon_type != expedition_type: 
            chance_to_change_type = random.randint(1,4)
            if chance_to_change_type == 4: # 1 chance / 4
                pigeon_type = expedition_type

        expedition = TR_Expedition.objects.filter(lvl=expedition_lvl)[0]

        lvl_info = TR_Lvl_info.objects.filter(lvl=player.lvl)[0]
        nb_pigeons = Pigeon.objects.filter(player_id=user.id, is_sold=False).count()
        
        if nb_pigeons >= lvl_info.max_pigeons: 
            return 'Error too many pigeons'
        if player.seeds < expedition.seeds: 
            return 'Not enough seeds'
        player.seeds = player.seeds - expedition.seeds
        player.save()
        
        p = TR_Pigeon.objects.filter(lvl_expedition=expedition_lvl, pigeon_type=pigeon_type)[0]
        logging.debug(str(p))


        luck_value = random.randint(1,100)
        phys_atk = int(luck_value/100*(p.max_phys_atk - p.min_phys_atk))+p.min_phys_atk
        magic_atk = int(luck_value/100*(p.max_magic_atk - p.min_magic_atk))+p.min_magic_atk
        shield = int(luck_value/100*(p.max_shield - p.min_shield))+p.min_shield
        drop_min = int(luck_value/100*(expedition.max_drop_minute - expedition.min_drop_minute))+expedition.min_drop_minute
        feathers = int(luck_value/100*(expedition.max_feathers - expedition.min_feathers))+expedition.min_feathers

        random_src = random.randint(0,len(p.src) - 1)

        creation_time = timezone.now()
        active_time = creation_time + timedelta(0,expedition.duration)

        new_pigeon = Pigeon(player_id=user.id, pigeon_type=p.pigeon_type, 
            name=p.name[random_src],src=p.src[random_src],pigeon_id=p.pigeon_id,luck=luck_value,
            lvl=expedition_lvl, phys_atk=phys_atk,magic_atk=magic_atk,shield=shield,
            droppings_minute=drop_min,feathers=feathers,
            creation_time=creation_time,active_time=active_time)
        new_pigeon.save()
        expeditions = Pigeon.objects.filter(player_id=user.id, is_open=False)  
        
    return list(expeditions.values())


def set_in_team(user, pigeon_id):

    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(player_id=user.id, is_sold=False, is_open=True)
        logging.debug("------"+str(pigeons))


        if int(pigeon_id) not in pigeons.values_list('id',flat=True):
            return 'Error: wrong id'
        
        pigeon_to_update = pigeons.filter(id = pigeon_id)[0]

        pigeon_to_update.is_in_team = not pigeon_to_update.is_in_team

        nb_in_team = pigeons.filter(is_in_team = True).count()

        if nb_in_team > 5:
            return 'Error : Too many in team'

        pigeon_to_update.save()

    return PigeonSerializer(pigeon_to_update).data


def organise_defenders(user, pigeon_ids):

    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(player_id=user.id, is_sold=False, is_open=True)

        if not all(int(p) in pigeons.values_list('id',flat=True) for p in pigeon_ids): 
            return 'Error: wrong id'
        
        previous_defenders = pigeons.exclude(defender_pos__isnull=True)
        previous_defenders.update(defender_pos=None)

        def_pos = 1
        for p in pigeon_ids:
            pigeons.filter(id=int(p)).update(defender_pos=def_pos)
            def_pos = def_pos + 1

        return list(pigeons.values())

def activate_pigeon(user, pigeon_id):
    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(player_id=user.id, is_sold=False, is_open=False)

        if int(pigeon_id) not in pigeons.values_list('id',flat=True):
            return 'Error: wrong id'
        
        pigeon_to_activate = pigeons.filter(id = pigeon_id)[0]

        if timezone.now() < pigeon_to_activate.active_time:
            return 'Error: pigeon not yet active !'

        pigeon_to_activate.is_open = True

        pigeon_to_activate.save()
    return PigeonSerializer(pigeon_to_activate).data

def sell_pigeon(user, pigeon_id):
    with transaction.atomic():
        pigeons = Pigeon.objects.select_for_update().filter(player_id=user.id, is_sold=False, is_open=True)

        if int(pigeon_id) not in pigeons.values_list('id',flat=True):
            return 'Error: wrong id'
    
        max_feathers = TR_Lvl_info.objects.get(lvl=user.player.lvl).max_feathers
        
        pigeon_to_sell = pigeons.filter(id = pigeon_id)[0]

        feathers_to_apply = user.player.feathers + pigeon_to_sell.feathers

        user.player.feathers = min(feathers_to_apply, max_feathers)

        pigeon_to_sell.is_sold = True

        pigeon_to_sell.save()
        user.player.save()
    return PigeonSerializer(pigeon_to_sell).data
