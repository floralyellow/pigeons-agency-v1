from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from rest_framework.views import APIView

from ..exceptions.custom_exceptions import ServiceException
from ..models.attack import Attack, AttackSerializer
from ..models.pigeon import Pigeon, PigeonSerializer
from ..models.player import User, UserSerializer
from ..services import attack_service, notification_service, update_service
from ..utils.validators import InputValidator


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

        all_attacks = Attack.objects.filter(attacker_id=player.id) | Attack.objects.filter(
            defender_id=player.id
        )

        ordered_attacks = all_attacks.order_by("-created_at")
        users = attack_service.get_ordered_attack_list(request.user)

        notification_service.remove_notifs(player)

        message = {
            "user": UserSerializer(request.user).data,
            "users": users,
            "attacks": AttackSerializer(ordered_attacks, many=True).data,
        }

        return JsonResponse({"message": message})


class AttackMessageDetailsView(APIView):
    """
    Returns details for an attack or defense
    """

    def post(self, request):
        update_service.update_user_values(request.user)

        attack_id = InputValidator.get_key(request, "a_id")

        player = request.user.player

        all_player_attacks = Attack.objects.filter(attacker_id=player.id) | Attack.objects.filter(
            defender_id=player.id
        )

        try:
            selected_attack = all_player_attacks.get(id=attack_id)
        except ObjectDoesNotExist:
            raise ServiceException("Error: Invalid id !")

        if selected_attack.attacker_id == player.id:
            defender = User.objects.get(id=selected_attack.defender_id)
        else:
            defender = User.objects.get(id=selected_attack.attacker_id)

        attack_pigeons = Pigeon.objects.filter(
            attackpigeon__attack_id=selected_attack.id, attackpigeon__is_attacker=True
        )
        defend_pigeons = Pigeon.objects.filter(
            attackpigeon__attack_id=selected_attack.id, attackpigeon__is_attacker=False
        )

        message = {
            "user": UserSerializer(request.user).data,
            "attack": AttackSerializer(selected_attack).data,
            "attack_pigeons": PigeonSerializer(attack_pigeons, many=True).data,
            "defend_pigeons": PigeonSerializer(defend_pigeons, many=True).data,
            "defender": UserSerializer(defender).data,
        }

        return JsonResponse({"message": message})
