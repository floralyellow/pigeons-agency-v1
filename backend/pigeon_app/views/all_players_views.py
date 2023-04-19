from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.views import APIView

from ..models.player import UserSerializer
from ..services import attack_service, update_service


class AllPlayersView(APIView):

    # get user info
    def get(self, request):

        update_service.update_user_values(request.user)

        users = UserSerializer(
            User.objects.order_by("-player__military_score", "-player__lvl"), many=True
        ).data

        return JsonResponse(
            {"message": {"user": UserSerializer(request.user).data, "users": users}}
        )


class AllPlayersForAttackView(APIView):

    # get user info
    def get(self, request):
        """
        return list of users in order :
        - difference in lvl
        - lvl desc
        - difference in military score
        - military score desc
        """

        update_service.update_user_values(request.user)

        users = attack_service.get_ordered_attack_list(request.user)
        import logging
        logging.info(users)

        return JsonResponse(
            {"message": {"user": UserSerializer(request.user).data, "users": users}}
        )
