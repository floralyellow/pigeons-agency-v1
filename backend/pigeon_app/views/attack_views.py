from django.http import JsonResponse
from rest_framework.views import APIView

from ..models.attack_pigeon import AttackPigeonSerializer
from ..models.player import UserSerializer
from ..services import attack_service, update_service
from ..utils.validators import InputValidator


class AttackView(APIView):
    def post(self, request):
        update_service.update_user_values(request.user)

        attack_team = InputValidator.get_key(request, "a_team")
        target_id = InputValidator.get_key(request, "u_id")

        InputValidator.validate_is_int(target_id)
        InputValidator.validate_is_in_values(attack_team, ["A", "B"])

        attack, pigeons = attack_service.attack_player(request.user, int(target_id), attack_team)
        pigeons_to_send = AttackPigeonSerializer(pigeons, many=True).data
        message = {
            "user": UserSerializer(request.user).data,
            "attack": attack,
            "attack_pigeons": pigeons_to_send,
        }

        return JsonResponse({"message": message})
