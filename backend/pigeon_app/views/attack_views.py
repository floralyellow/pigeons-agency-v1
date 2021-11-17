
from ..models import TR_Lvl_info
from ..models import TR_Effect
from ..models import TR_Expedition
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..models import Player, Pigeon
from pigeon_app.models.player import UserSerializer
from django.db import transaction
from ..services import update_service, attack_service
import json
import logging

class AttackInitView(APIView):

    # init attack
    def post(self, request):
        update_service.update_user_values(request.user)
        if request.user.player.attacking_id is not None:
            return JsonResponse({'message': 'Error: In attack !'})
        if 'u_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        target_id = request.POST.get('u_id')
        if not target_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})

        attacking_pigeons, defending_pigeons = attack_service.init_attack(request.user, target_id)

        return JsonResponse({'message': {'user': UserSerializer(request.user).data, 'attacking_pigeons' : attacking_pigeons, 'defending_pigeons' : defending_pigeons}})

class AttackView(APIView):

    # attack player
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

        # only route where NEEDS to be in attack
        if request.user.player.attacking_id is None:
            return JsonResponse({'message': 'Error: Not in attack !'})

        o = attack_service.attack_player(request.user, pigeon_ids)
 
        return JsonResponse({'message': o})
