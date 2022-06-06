from pigeon_app.models.player import UserSerializer
from ..models import Pigeon
from rest_framework.views import APIView
from ..services import pigeon_service, update_service
from ..utils.validator import InputValidator
from ..utils.standard_response import StandardJsonResponse as SJR


class PigeonView(APIView):
    # Get all pigeons of user
    def get(self, request):

        update_service.update_user_values(request.user)
        user_id = request.user.id
        pigeons = list(Pigeon.objects.filter(player_id=user_id, is_sold=False).values())
        return SJR({'user': UserSerializer(request.user).data, 'pigeons' : pigeons})



    # create pigeon
    def post(self, request):

        update_service.update_user_values(request.user)
        keys_to_validate = ['exp_lvl', 'exp_type']
        InputValidator.validate_keys_exist_in_post_data(request, keys_to_validate)
        expedition_lvl = request.POST.get('exp_lvl')
        expedition_type = request.POST.get('exp_type')

        InputValidator.validate_is_int_in_range(expedition_lvl, 1, 30+1, 'exp_lvl')
        InputValidator.validate_is_int_in_range(expedition_type, 1, 4+1, 'exp_type')

        expeditions = pigeon_service.create_pigeon(request.user, expedition_lvl, expedition_type)

        return SJR({'user': UserSerializer(request.user).data, 'expeditions' : expeditions})

class ExpeditionView(APIView):

    # get expeditions
    def get(self, request):

        update_service.update_user_values(request.user)
        user_id = request.user.id
        expeditions = list(Pigeon.objects.filter(player_id=user_id, is_open=False).values())
        nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return SJR({'user': UserSerializer(request.user).data, 'expeditions' : expeditions, 'nb_pigeons' : nb_pigeons, 'droppings_minute' : droppings_minute})



class PigeonTeamAView(APIView):

    # set/unset in team
    def post(self, request):

        update_service.update_user_values(request.user)

        key_to_validate = 'p_id'
        InputValidator.validate_keys_exist_in_post_data(request, key_to_validate)
        pigeon_id = request.POST.get(key_to_validate)
        InputValidator.validate_is_int(pigeon_id, key_to_validate)

        message = pigeon_service.set_in_team_A(request.user, pigeon_id)

        return SJR(message)

class PigeonTeamBView(APIView):

    # set/unset in team
    def post(self, request):

        update_service.update_user_values(request.user)

        key_to_validate = 'p_id'
        InputValidator.validate_keys_exist_in_post_data(request, key_to_validate)
        pigeon_id = request.POST.get(key_to_validate)
        InputValidator.validate_is_int(pigeon_id, key_to_validate)

        message = pigeon_service.set_in_team_B(request.user, pigeon_id)

        return SJR(message)


class PigeonActivateView(APIView):

    # activatePigeon
    def post(self, request):

        update_service.update_user_values(request.user)
        key_to_validate = 'p_id'
        InputValidator.validate_keys_exist_in_post_data(request, key_to_validate)
        pigeon_id = request.POST.get(key_to_validate)
        InputValidator.validate_is_int(pigeon_id, key_to_validate)

        message = pigeon_service.activate_pigeon(request.user, pigeon_id)
        return SJR(message)

class PigeonSellView(APIView):

    # sellPigeon
    def post(self, request):

        update_service.update_user_values(request.user)
        key_to_validate = 'p_id'
        InputValidator.validate_keys_exist_in_post_data(request, key_to_validate)
        pigeon_id = request.POST.get(key_to_validate)
        InputValidator.validate_is_int(pigeon_id, key_to_validate)

        message = pigeon_service.sell_pigeon(request.user, pigeon_id)
        return SJR(message)
