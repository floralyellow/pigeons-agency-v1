from ..errors.ServiceError import ServiceError
from rest_framework.views import APIView
from pigeon_app.models.player import UserSerializer
from pigeon_app.models.attack_pigeon import AttackPigeonSerializer
from ..services import update_service, attack_service
from ..utils.validator import InputValidator
from ..utils.standard_response import StandardJsonResponse as SJR

class AttackView(APIView):

    def post(self, request):
        update_service.update_user_values(request.user)

        keys_to_validate = ['u_id','a_team']
        InputValidator.validate_keys_exist_in_post_data(keys_to_validate)
        attack_team = request.POST.get('a_team')
        target_id = request.POST.get('u_id')
        InputValidator.validate_is_int(target_id)
        InputValidator.validate_is_in_values(attack_team, ['A','B'])

        # TODO test
        try:
            attack, pigeons = attack_service.attack_player(request.user, int(target_id), attack_team)
            pigeons_to_send = AttackPigeonSerializer(pigeons, many=True).data
            message = {'user': UserSerializer(request.user).data, \
                    'attack' : attack, \
                    'attack_pigeons' : pigeons_to_send, 
                    }
        except ServiceError as e:
            message = e.args[0]

        return SJR(message) 
