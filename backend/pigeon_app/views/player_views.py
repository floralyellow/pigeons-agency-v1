from django.db import transaction
from django.http import JsonResponse
from rest_framework.views import APIView

from ..exceptions.custom_exceptions import BackendException, ServiceException
from ..models import TR_Lvl_info
from ..models.player import UserSerializer
from ..services import pigeon_service, update_service
from ..utils.commons import NEEDED_DROPPINGS_TO_USE_BUCKET_RATIO


class PlayerView(APIView):

    # get user info
    def get(self, request):

        update_service.update_user_values(request.user)

        nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse(
            {
                "message": {
                    "user": UserSerializer(request.user).data,
                    "nb_pigeons": nb_pigeons,
                    "droppings_minute": droppings_minute,
                }
            }
        )


class PlayerLvlupView(APIView):

    # lvl up
    def post(self, request):

        update_service.update_user_values(request.user)

        with transaction.atomic():
            player = request.user.player

            feathers = player.feathers
            player_lvl = player.lvl

            feathers_to_lvlup = TR_Lvl_info.objects.filter(lvl=player_lvl)[0].max_feathers
            max_seeds_next_lvl = TR_Lvl_info.objects.filter(lvl=player_lvl + 1)[0].max_seeds

            if feathers_to_lvlup > feathers:
                raise ServiceException("Error: Not enough feathers !")

            player.feathers = 0
            player.lvl = player.lvl + 1
            player.seeds = max_seeds_next_lvl
            player.save()

            nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse(
            {
                "message": {
                    "user": UserSerializer(request.user).data,
                    "nb_pigeons": nb_pigeons,
                    "droppings_minute": droppings_minute,
                }
            }
        )


class PlayerUseBucketView(APIView):

    # use bucket
    def post(self, request):

        update_service.update_user_values(request.user)

        with transaction.atomic():
            player = request.user.player

            lvl_info = TR_Lvl_info.objects.filter(lvl=player.lvl)[0]

            cost_droppings = int(lvl_info.max_droppings * NEEDED_DROPPINGS_TO_USE_BUCKET_RATIO)

            if cost_droppings > player.droppings:
                raise ServiceException("Error: Not enough droppings !")

            player.droppings = player.droppings - cost_droppings
            player.seeds = lvl_info.max_seeds
            player.save()

            nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse(
            {
                "message": {
                    "user": UserSerializer(request.user).data,
                    "nb_pigeons": nb_pigeons,
                    "droppings_minute": droppings_minute,
                }
            }
        )


class PlayerChangeDefenseTeamView(APIView):
    def post(self, request):
        """
        update defense team used in pvp attacks
        """

        update_service.update_user_values(request.user)
        player = request.user.player

        if player.defense_team == "A":
            player.defense_team = "B"
        elif player.defense_team == "B":
            player.defense_team = "A"
        else:
            raise BackendException("Error: Unexpected defense team !")

        player.save()

        return JsonResponse({"message": {"user": UserSerializer(request.user).data}})


class PlayerChangeDarkModeView(APIView):
    def post(self, request):
        """ """

        update_service.update_user_values(request.user)
        player = request.user.player

        player.is_dark_mode = not player.is_dark_mode
        player.save()

        return JsonResponse({"message": {"user": UserSerializer(request.user).data}})


class PlayerDoneTutorialView(APIView):
    def post(self, request):
        """ """

        update_service.update_user_values(request.user)
        player = request.user.player

        player.is_tutorial_done = True
        player.save()

        return JsonResponse({"message": {"user": UserSerializer(request.user).data}})
