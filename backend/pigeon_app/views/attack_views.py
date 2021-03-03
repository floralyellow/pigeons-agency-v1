
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
