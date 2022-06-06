from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from pigeon_app.models.player import UserSerializer
from ..services import update_service
import logging

class AllPlayersView(APIView):

    # get user info
    def get(self, request):

        update_service.update_user_values(request.user)

        users = UserSerializer(User.objects.order_by('-player__military_score', '-player__lvl'), many=True).data

        return JsonResponse({'message': {'user': UserSerializer(request.user).data,'users' : users}})

class AllPlayersForAttackView(APIView):

    # get user info
    def get(self, request):
        '''
        return list of users in order : 
        - difference in lvl
        - lvl desc
        - difference in military score
        - military score desc
        ''' 

        update_service.update_user_values(request.user)

        users = UserSerializer(User.objects \
            .select_related('player') \
            .extra(select={'offset_military': 'abs(pigeon_app_player.military_score - %s)'},select_params=(request.user.player.military_score,),)
            .extra(select={'offset_lvl': 'abs(pigeon_app_player.lvl - %s)'},select_params=(request.user.player.lvl,),)
            .order_by('offset_lvl', '-player__lvl', 'offset_military', '-player__military_score'), many=True).data

        return JsonResponse({'message': {'user': UserSerializer(request.user).data,'users' : users}})