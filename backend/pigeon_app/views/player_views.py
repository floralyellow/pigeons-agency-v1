
from ..models import TR_Pigeon
from ..models import TR_Lvl_info
from ..models import TR_Effect
from ..models import TR_Expedition
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from ..models import Player
from pigeon_app.models.player import UserSerializer
from django.db import transaction
from ..services import update_service, pigeon_service
import logging

class PlayerView(APIView):

    # get user info
    def get(self, request):

        if request.user.player.attacking_id is not None:
            return JsonResponse({'message': 'Error: In attack !'})
        update_service.update_user_values(request.user)

        nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse({'message': {'user': UserSerializer(request.user).data, 'nb_pigeons' : nb_pigeons, 'droppings_minute' : droppings_minute}})


class PlayerLvlupView(APIView):

    # lvl up
    def post(self, request):

        if request.user.player.attacking_id is not None:
            return JsonResponse({'message': 'Error: In attack !'})
        update_service.update_user_values(request.user)

        with transaction.atomic():
            player = request.user.player

            feathers = player.feathers
            player_lvl = player.lvl

            feathers_to_lvlup = TR_Lvl_info.objects.filter(lvl=player_lvl)[0].max_feathers

            if feathers_to_lvlup > feathers:
                return JsonResponse({'message': 'Error: Not enough feathers'})

            player.feathers = 0
            player.lvl = player.lvl + 1
            player.save()

        return JsonResponse({'message': UserSerializer(request.user).data})

class PlayerUseBucketView(APIView):

    # use bucket
    def post(self, request):

        if request.user.player.attacking_id is not None:
            return JsonResponse({'message': 'Error: In attack !'})
        update_service.update_user_values(request.user)

        with transaction.atomic():
            player = request.user.player

            lvl_info = TR_Lvl_info.objects.filter(lvl=player.lvl)[0]

            if lvl_info.max_droppings > player.droppings:
                return JsonResponse({'message': 'Error: Not enough droppings'})

            player.droppings = 0
            player.seeds = lvl_info.max_seeds
            player.save()

        return JsonResponse({'message': UserSerializer(request.user).data})
