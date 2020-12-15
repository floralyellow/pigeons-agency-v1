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
from ..models import TR_Pigeon
from ..models import TR_Lvl_info
from ..models import TR_Effect
import random

class PigeonView(APIView):
    # Get all pigeons of user
    def get(self, request):
        user_id = request.user.id
        pigeons = Pigeon.objects.filter(player_id=user_id)
        return JsonResponse(list(pigeons.values()), safe=False)


    # create pigeon
    def post(self, request):
        user_id = request.user.id
        lvl = 1 # Get this from POST body expedition lvl + check seeds
        logging.debug("------"+str(lvl))
        possible_pigeons = TR_Pigeon.objects.filter(lvl_expedition=lvl)
        test_random = random.randint(0, len(possible_pigeons)-1)
        logging.debug("------"+str(test_random))
        logging.debug("------"+str(possible_pigeons[test_random]))
        tr_pigeon = possible_pigeons[test_random]



        new_pigeon = Pigeon(player_id=user_id, name=tr_pigeon.name, attack=tr_pigeon.max_atk)
        new_pigeon.save()
        pigeons = Pigeon.objects.filter(player_id=user_id)     
        #return JsonResponse(possible_pigeons[test_random], safe=False)

        return JsonResponse(list(pigeons.values()), safe=False)
