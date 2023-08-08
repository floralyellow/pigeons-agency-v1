from django.http import JsonResponse
from rest_framework.views import APIView

from ..models.player import UserSerializer
from ..models.attack import Attack, AttackSerializer

from ..services import attack_service, update_service
from ..utils.validators import InputValidator
import logging


class AttackView(APIView):
    def post(self, request):
        update_service.update_user_values(request.user)

        attack_team = InputValidator.get_key(request, "a_team")
        target_id = InputValidator.get_key(request, "u_id")

        InputValidator.validate_is_int(target_id)
        InputValidator.validate_is_in_values(attack_team, ["A", "B"])

        attack, attack_pigeons, defend_pigeons, defender = attack_service.attack_player(
            request.user, int(target_id), attack_team
        )

        users = attack_service.get_ordered_attack_list(request.user)

        message = {
            "user": UserSerializer(request.user).data,
            "attack": attack,
            "attack_pigeons": list(attack_pigeons.values()),
            "defend_pigeons": list(defend_pigeons.values()),
            "defender": UserSerializer(defender).data,
            "users": users,
        }

        return JsonResponse({"message": message})
    
class AttackMessagesView(APIView):
    """
    Returns all attacks and defenses in which a player has been
    """
    def get(self, request):
        update_service.update_user_values(request.user)

        player = request.user.player

        all_attacks = Attack.objects.filter(attacker_id=player.id) | Attack.objects.filter(defender_id=player.id)

        ordered_attacks = all_attacks.order_by('-created_at')

        message = {
            "attacks": AttackSerializer(ordered_attacks, many=True).data,
        }

        return JsonResponse({"message": message})

