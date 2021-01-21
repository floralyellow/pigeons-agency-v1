from pigeon_app.models.player import UserSerializer
from pigeon_app.models.player import PlayerSerializer
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
from ..models import TR_Effect
from ..models import TR_Expedition
from datetime import datetime,timedelta
import random
from django.db import transaction

class PigeonView(APIView):
    # Get all pigeons of user
    def get(self, request):
        user_id = request.user.id
        pigeons = Pigeon.objects.filter(player_id=user_id)
        return JsonResponse(list(pigeons.values()), safe=False)


    # create pigeon
    def post(self, request):
        logging.debug("------"+str(request))

        if 'exp_lvl' not in request.POST:
            return JsonResponse({'message': 'Error: No expedition_lvl'})
        expedition_lvl = request.POST.get('exp_lvl')
        if not expedition_lvl.isdigit() or not int(expedition_lvl) in range(1,30):
            return JsonResponse({'message': 'Error: invalid input'})

        user_id = request.user.id
        with transaction.atomic():
            player = Player.objects.select_for_update().filter(user_id=user_id)[0]
            if player.lvl < int(expedition_lvl):
                return JsonResponse({'message': 'Invalid lvl'})

            expedition = TR_Expedition.objects.filter(lvl=expedition_lvl)[0]

            lvl_info = TR_Lvl_info.objects.filter(lvl=player.lvl)[0]
            nb_pigeons = Pigeon.objects.filter(player_id=user_id, is_sold=False).count()
            
            if nb_pigeons >= lvl_info.max_pigeons: 
                return JsonResponse({'message': 'Too many pigeons'})

            if player.seeds < expedition.seeds: 
                return JsonResponse({'message': 'Not enough seeds'})
            player.seeds = player.seeds - expedition.seeds
            player.save()
            
            possible_pigeons = TR_Pigeon.objects.filter(lvl_expedition=expedition_lvl)
            weights = possible_pigeons.values_list('coef_chance_rate',flat=True)
            p = random.choices(population = possible_pigeons, weights = weights, k=1)[0]

            luck_value = random.randint(1,100)
            element = random.randint(1,3)
            atk = int(luck_value/100*(p.max_atk - p.min_atk))+p.min_atk
            life = int(luck_value/100*(p.max_life - p.min_life))+p.min_life
            shield = int(luck_value/100*(p.max_shield - p.min_shield))+p.min_shield
            drop_min = int(luck_value/100*(expedition.max_drop_minute - expedition.min_drop_minute))+expedition.min_drop_minute
            feathers = int(luck_value/100*(expedition.max_feathers - expedition.min_feathers))+expedition.min_feathers
            creation_time = timezone.now()
            active_time = creation_time + timedelta(0,expedition.duration)

            new_pigeon = Pigeon(player_id=user_id, pigeon_type=p.pigeon_type, 
                name=p.name,pigeon_id=p.pigeon_id,luck=luck_value,
                element=element, attack=atk,life=life,shield=shield,
                speed=p.speed,droppings_minute=drop_min,feathers=feathers,
                creation_time=creation_time,active_time=active_time)
            new_pigeon.save()
            pigeons = Pigeon.objects.filter(player_id=user_id)  
            return JsonResponse(list(pigeons.values()), safe=False)

class PigeonAttackerView(APIView):

    # set attacker
    def post(self, request):
        logging.debug("------"+str(request))

        if 'p_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        pigeon_id = request.POST.get('p_id')
        if not pigeon_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})

        user_id = request.user.id
        with transaction.atomic():
            pigeons = Pigeon.objects.filter(player_id=user_id, is_sold=False, is_open=True)
            logging.debug("------"+str(pigeons))


            if int(pigeon_id) not in pigeons.values_list('id',flat=True):
                return JsonResponse({'message': 'Error: wrong id'})
            
            pigeon_to_update = pigeons.filter(id = pigeon_id)[0]

            pigeon_to_update.is_attacker = not pigeon_to_update.is_attacker

            nb_attackers = pigeons.select_for_update().filter(is_attacker = True).count()

            if nb_attackers > 5:
                return JsonResponse({'message': 'Too many atk'})

            pigeon_to_update.save()
            return JsonResponse(list(pigeons.values()), safe=False)

class PigeonActivateView(APIView):

    # activatePigeon
    def post(self, request):
        logging.debug("------"+str(request))

        if 'p_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        pigeon_id = request.POST.get('p_id')
        if not pigeon_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})

        user_id = request.user.id
        with transaction.atomic():
            pigeons = Pigeon.objects.filter(player_id=user_id, is_sold=False, is_open=False)
            logging.debug("------"+str(pigeons))


            if int(pigeon_id) not in pigeons.values_list('id',flat=True):
                return JsonResponse({'message': 'Error: wrong id'})
            
            pigeon_to_activate = pigeons.filter(id = pigeon_id)[0]

            if timezone.now() < pigeon_to_activate.active_time:
                return JsonResponse({'message': 'Error: pigeon not yet active !'})

            pigeon_to_activate.is_open = True

            pigeon_to_activate.save()
            return JsonResponse(list(pigeons.values()), safe=False)

class PigeonSellView(APIView):

    # sellPigeon
    def post(self, request):
        logging.debug("------"+str(request))

        if 'p_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        pigeon_id = request.POST.get('p_id')
        if not pigeon_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})

        user_id = request.user.id
        with transaction.atomic():
            pigeons = Pigeon.objects.filter(player_id=user_id, is_sold=False, is_open=True)
            logging.debug("------"+str(pigeons))


            if int(pigeon_id) not in pigeons.values_list('id',flat=True):
                return JsonResponse({'message': 'Error: wrong id'})
            
            pigeon_to_sell = pigeons.filter(id = pigeon_id)[0]

            player = Player.objects.select_for_update().filter(user_id=user_id)[0]
            player.feathers += pigeon_to_sell.feathers

            pigeon_to_sell.is_sold = True

            pigeon_to_sell.save()
            player.save()
            return JsonResponse(list(pigeons.values()), safe=False)