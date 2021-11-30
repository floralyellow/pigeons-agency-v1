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
import json
from ..models import TR_Pigeon
from ..models import TR_Lvl_info
from ..models import TR_Expedition
from datetime import datetime,timedelta
import random
from django.db import transaction
from ..services import pigeon_service, update_service

class PigeonView(APIView):
    # Get all pigeons of user
    def get(self, request):

        update_service.update_user_values(request.user)
        user_id = request.user.id
        pigeons = list(Pigeon.objects.filter(player_id=user_id, is_sold=False).values())
        return JsonResponse({'message': {'user': UserSerializer(request.user).data, 'pigeons' : pigeons}})



    # create pigeon
    def post(self, request):

        update_service.update_user_values(request.user)
        if 'exp_lvl' not in request.POST:
            return JsonResponse({'message': 'Error: No expedition_lvl'})
        if 'exp_type' not in request.POST:
            return JsonResponse({'message': 'Error: No expedition_type'})
        expedition_lvl = request.POST.get('exp_lvl')
        expedition_type = request.POST.get('exp_type')
        if not expedition_lvl.isdigit() or not int(expedition_lvl) in range(1,30+1):
            return JsonResponse({'message': 'Error: invalid input lvl'})
        if not expedition_type.isdigit() or not int(expedition_type) in range(1,4+1):
            return JsonResponse({'message': 'Error: invalid input type'})

        expeditions = pigeon_service.create_pigeon(request.user, expedition_lvl, expedition_type)

        return JsonResponse({'message': {'user': UserSerializer(request.user).data, 'expeditions' : expeditions}})

class ExpeditionView(APIView):

    # get expeditions
    def get(self, request):

        update_service.update_user_values(request.user)
        user_id = request.user.id
        expeditions = list(Pigeon.objects.filter(player_id=user_id, is_open=False).values())
        nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse({'message': {'user': UserSerializer(request.user).data, 'expeditions' : expeditions, 'nb_pigeons' : nb_pigeons, 'droppings_minute' : droppings_minute}})



class PigeonTeamView(APIView):

    # set/unset in team
    def post(self, request):

        update_service.update_user_values(request.user)

        if 'p_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        pigeon_id = request.POST.get('p_id')
        if not pigeon_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})
        
        message = pigeon_service.set_in_team(request.user, pigeon_id)

        return JsonResponse({'message': message})


class PigeonDefenderOrderView(APIView):
    # organise defenders
    def post(self, request):

        update_service.update_user_values(request.user)

        try:
            input = json.loads(request.body)
            logging.debug(input)
            pigeon_ids = input["pigeon_ids"]

        except (ValueError, KeyError) as e:  
            return JsonResponse({'message': 'Error: wrong input1'})
        
        if not isinstance(pigeon_ids, list):
            return JsonResponse({'message': 'Error: wrong input2'})

        if not len(pigeon_ids) == 5:
            return JsonResponse({'message': 'Error: wrong input3'})

        if not all(isinstance(x, int) for x in pigeon_ids): 
            return JsonResponse({'message': 'Error: invalid input4'})
            
        if not len(pigeon_ids) == len(set(pigeon_ids)): 
            return JsonResponse({'message': 'Error: invalid input5'})

        message = pigeon_service.organise_defenders(request.user, pigeon_ids)

        return JsonResponse({'message': message})

class PigeonActivateView(APIView):

    # activatePigeon
    def post(self, request):

        update_service.update_user_values(request.user)
        if 'p_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        pigeon_id = request.POST.get('p_id')
        if not pigeon_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})

        message = pigeon_service.activate_pigeon(request.user, pigeon_id)
        logging.debug('yee1')
        return JsonResponse({'message': message})

class PigeonSellView(APIView):

    # sellPigeon
    def post(self, request):

        update_service.update_user_values(request.user)
        if 'p_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        pigeon_id = request.POST.get('p_id')
        if not pigeon_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})

        message = pigeon_service.sell_pigeon(request.user, pigeon_id)

        return JsonResponse({'message': message})
