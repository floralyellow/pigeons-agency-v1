from django.http import JsonResponse
from ..models import Player
from ..models import Pigeon
import logging


def index(request):
    logging.debug("------"+str(request))
    return JsonResponse({ "status": "I'm here" })

def create_test_player(request):
    logging.debug("------"+str(request))
    player = Player(username='test')
    logging.debug("------"+str(player))
    player.save()
    return JsonResponse({ "status": player.username })

def get_test_players(request):
    logging.debug("------"+str(request))
    players = Player.objects.all()
    return JsonResponse({ "status": players })