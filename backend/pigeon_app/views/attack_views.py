
from ..models import TR_Lvl_info
from ..models import TR_Expedition
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..models import Player, Pigeon
from pigeon_app.models.player import UserSerializer
from pigeon_app.models.attack_pigeon import AttackPigeonSerializer
from django.db import transaction
from ..services import update_service, attack_service
import json
import logging

class AttackView(APIView):

    # init attack
    def post(self, request):
        update_service.update_user_values(request.user)

        if 'u_id' not in request.POST:
            return JsonResponse({'message': 'Error: No post info'})
        target_id = request.POST.get('u_id')
        if not target_id.isdigit() :
            return JsonResponse({'message': 'Error: invalid input'})

        attack, pigeons = attack_service.attack_player(request.user, target_id)

        pigeons_to_send = AttackPigeonSerializer(pigeons, many=True).data

        return JsonResponse({'message': {'user': UserSerializer(request.user).data, \
                            'attack' : attack, \
                            'attack_pigeons' : pigeons_to_send, 
                            }}) 
