
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
#from ..services import player_service


class PlayerView(APIView):

    # get user info
    def get(self, request):
        user_id = request.user.id
        player = Player.objects.filter(user_id=user_id)[0]

        return JsonResponse({'message': UserSerializer(request.user).data})


class PlayerLvlupView(APIView):

    # slvl up
    def post(self, request):
        user_id = request.user.id
        with transaction.atomic():
            player = Player.objects.select_for_update().filter(user_id=user_id)[0]

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
        user_id = request.user.id
        with transaction.atomic():
            player = Player.objects.select_for_update().filter(user_id=user_id)[0]

            droppings = player.droppings
            player_lvl = player.lvl

            lvl_info = TR_Lvl_info.objects.filter(lvl=player_lvl)[0]

            if lvl_info.max_droppings > droppings:
                return JsonResponse({'message': 'Error: Not enough droppings'})

            player.droppings = 0
            player.seeds = lvl_info.max_seeds
            player.save()

        return JsonResponse({'message': UserSerializer(request.user).data})
