from django.http import JsonResponse
from pigeon_app.models.player import UserSerializer
from rest_framework.views import APIView

from ..models import Pigeon
from ..services import pigeon_service, update_service
from ..utils.validators import InputValidator


class PigeonView(APIView):
    # Get all pigeons of user
    def get(self, request):

        update_service.update_user_values(request.user)
        user_id = request.user.id
        pigeons = list(Pigeon.objects.filter(player_id=user_id, is_sold=False).values())
        return JsonResponse(
            {"message": {"user": UserSerializer(request.user).data, "pigeons": pigeons}}
        )

    # create pigeon
    def post(self, request):

        update_service.update_user_values(request.user)

        expedition_lvl = InputValidator.get_key(request, "exp_lvl")
        expedition_type = InputValidator.get_key(request, "exp_type")

        InputValidator.validate_is_int_in_range(expedition_lvl, 1, 30 + 1)
        InputValidator.validate_is_int_in_range(expedition_type, 1, 4 + 1)

        expeditions = pigeon_service.create_pigeon(request.user, expedition_lvl, expedition_type)

        return JsonResponse(
            {"message": {"user": UserSerializer(request.user).data, "expeditions": expeditions}}
        )


class ExpeditionView(APIView):

    # get expeditions
    def get(self, request):

        update_service.update_user_values(request.user)
        user_id = request.user.id
        expeditions = list(Pigeon.objects.filter(player_id=user_id, is_open=False).values())
        nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse(
            {
                "message": {
                    "user": UserSerializer(request.user).data,
                    "expeditions": expeditions,
                    "nb_pigeons": nb_pigeons,
                    "droppings_minute": droppings_minute,
                }
            }
        )


class PigeonTeamAView(APIView):

    # set/unset in team
    def post(self, request):

        update_service.update_user_values(request.user)

        pigeon_id = InputValidator.get_key(request, "p_id")

        InputValidator.validate_is_int(pigeon_id)

        message = pigeon_service.set_in_team_A(request.user, pigeon_id)

        return JsonResponse({"message": message})


class PigeonTeamBView(APIView):

    # set/unset in team
    def post(self, request):

        update_service.update_user_values(request.user)

        pigeon_id = InputValidator.get_key(request, "p_id")

        InputValidator.validate_is_int(pigeon_id)

        message = pigeon_service.set_in_team_B(request.user, pigeon_id)

        return JsonResponse({"message": message})


class PigeonActivateView(APIView):

    # activatePigeon
    def post(self, request):

        update_service.update_user_values(request.user)

        pigeon_id = InputValidator.get_key(request, "p_id")

        InputValidator.validate_is_int(pigeon_id)

        message = pigeon_service.activate_pigeon(request.user, pigeon_id)
        return JsonResponse({"message": message})


class PigeonSellView(APIView):

    # sellPigeon
    def post(self, request):

        update_service.update_user_values(request.user)

        pigeon_id = InputValidator.get_key(request, "p_id")

        InputValidator.validate_is_int(pigeon_id)

        message = pigeon_service.sell_pigeon(request.user, pigeon_id)

        return JsonResponse({"message": message})
