from django.http import JsonResponse
from rest_framework.views import APIView

from ..models.adventure import AdventureSerializer
from ..models.adventure_attack import AdventureAttackSerializer
from ..models.player import UserSerializer
from ..models.pve_pigeon import PvePigeonSerializer
from ..services import adventure_service, pigeon_service, update_service
from ..utils.validators import InputValidator


class AdventureView(APIView):
    def get(self, request):
        update_service.update_user_values(request.user)

        adventure = adventure_service.get_adventure(request.user)

        adventure_pigeons = adventure_service.get_adventure_pigeons(
            adventure.lvl, adventure.encounter
        )

        nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse(
            {
                "message": {
                    "user": UserSerializer(request.user).data,
                    "nb_pigeons": nb_pigeons,
                    "droppings_minute": droppings_minute,
                    "adventure": AdventureSerializer(adventure).data,
                    "adventure_pigeons": PvePigeonSerializer(adventure_pigeons, many=True).data,
                }
            }
        )

    def post(self, request):
        """
        try pve adventure.
        expected post keys
            a_team : team of pigeons (A or B)

        """
        update_service.update_user_values(request.user)

        attack_team = InputValidator.get_key(request, "a_team")
        InputValidator.validate_is_in_values(attack_team, ["A", "B"])

        adventure_attack, current_adventure = adventure_service.try_adventure(
            request.user, attack_team
        )

        next_adventure = adventure_service.get_adventure(request.user)

        next_adventure_pigeons = adventure_service.get_adventure_pigeons(
            next_adventure.lvl, next_adventure.encounter
        )

        nb_pigeons, droppings_minute = pigeon_service.get_global_pigeon_info(request.user)

        return JsonResponse(
            {
                "message": {
                    "user": UserSerializer(request.user).data,
                    "nb_pigeons": nb_pigeons,
                    "droppings_minute": droppings_minute,
                    "adventure_attack": AdventureAttackSerializer(adventure_attack).data,
                    "current_adventure": AdventureSerializer(current_adventure).data,
                    "next_adventure": AdventureSerializer(next_adventure).data,
                    "next_adventure_pigeons": PvePigeonSerializer(
                        next_adventure_pigeons, many=True
                    ).data,
                }
            }
        )
