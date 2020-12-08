from django.http import JsonResponse
from ..models import Player
from ..models import Pigeon
import logging
from django.core import serializers


def index(request):
    logging.debug("------"+str(request))
    return JsonResponse({ "status": "I'm here" })

def test(request):
    logging.debug("------"+str(request))
    logging.debug("------"+str(request.POST))
    return JsonResponse({ "status": "e" })

def create_test_player(request):
    logging.debug("------"+str(request))
    player = Player(username='test',feathers=0)
    logging.debug("------"+str(player))
    player.save()
    return JsonResponse({ "status": player.username })

def get_test_players(request):
    logging.debug("------"+str(request))
    players = Player.objects.all()
    return JsonResponse(list(players.values()), safe=False)