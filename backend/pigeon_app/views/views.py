from pigeon_app.models.player import UserSerializer
from pigeon_app.models.player import PlayerSerializer
from django.http import JsonResponse
from django.contrib.auth.models import User
from ..models import Player
from ..models import Pigeon
import logging
from django.core import serializers
from rest_framework import viewsets
from rest_framework.views import APIView
from django.core.signals import request_finished
from django.dispatch import receiver
from django.db.models.signals import post_save
#from django.views.decorators.csrf import csrf_exempt
import random

# @receiver(post_save, sender=Player)
# def create_player(sender, instance, created, **kwargs):
#     """Create a matching profile whenever a user object is created."""
#     if created:
#         player, new = Player.objects.get_or_create(player=instance)


class UserViewSet(viewsets.ModelViewSet):
    '''model view set that generate automaticly get,post,patch, delete'''
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        '''limit queryset to user data'''
        queryset = self.queryset
        query_set = queryset.filter(id=self.request.user.id)
        return query_set
    
    def get_permissions(self):
        '''Allow anonymous users to post user'''
        if self.request.method == 'POST':
            return []
        return super().get_permissions()


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    '''signal receiver that create a player to every assosciated created User'''
    if created:
        Player.objects.create(user=instance)



class TestView(APIView):
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return JsonResponse(content)

    def post(self, request):
        content = {'message': 'Haa!'}
        return JsonResponse(content)


class PigeonView(APIView):
    # Get all pigeons of user
    def get(self, request):
        user_id = request.user.id
        pigeons = Pigeon.objects.filter(player_id=user_id)
        return JsonResponse(list(pigeons.values()), safe=False)


    # create pigeon
    def post(self, request):
        user_id = request.user.id
        pigeon = Pigeon(player_id=user_id, attack=int(random.randint(0, 400)))
        pigeon.save()
        pigeons = Pigeon.objects.filter(player_id=user_id)     
        return JsonResponse(list(pigeons.values()), safe=False)

    # @csrf_exempt 
    # def index(request):
    #     logging.debug("------"+str(request))
    #     return JsonResponse({"status": "I'm here"})

    # @csrf_exempt #For POST requests
    # def test(request):
    #     logging.debug("------"+str(request))
    #     logging.debug("------"+str(request.POST))
    #     return JsonResponse({ "status": "e" })


    # def get_test_players(request):
    #     logging.debug("------"+str(request))
    #     players = Player.objects.all()
    #     return JsonResponse(list(players.values()), safe=False)
