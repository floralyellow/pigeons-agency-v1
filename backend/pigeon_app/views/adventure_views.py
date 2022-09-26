from django.http import JsonResponse
from pigeon_app.models.adventure import AdventureSerializer
from pigeon_app.models.player import UserSerializer
from pigeon_app.models.pve_pigeon import PvePigeonSerializer
from rest_framework.views import APIView

from ..services import adventure_service, update_service


class AdventureView(APIView):
    def get(self, request):
        update_service.update_user_values(request.user)

        adventure = adventure_service.get_adventure(request.user)

        adventure_pigeons = adventure_service.get_adventure_pigeons(
            adventure.lvl, adventure.encounter
        )

        return JsonResponse(
            {
                "message": {
                    "user": UserSerializer(request.user).data,
                    "adventure": AdventureSerializer(adventure).data,
                    "adventure_pigeons": PvePigeonSerializer(adventure_pigeons, many=True).data,
                }
            }
        )

    def post(self, request):
        # TODO
        update_service.update_user_values(request.user)

        return None
