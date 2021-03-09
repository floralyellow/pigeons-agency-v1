from ..models import TR_Lvl_info
from ..models import TR_Effect
from ..models import TR_Expedition
from django.contrib.auth.models import User
from ..models import Player, Pigeon
from pigeon_app.models.player import UserSerializer
from django.db import transaction
from ..services import update_service, attack_service
import logging

def init_attack(user, target_id):

    with transaction.atomic():
        res = Player.objects.filter(id=target_id)

        if len(res) != 1 or target_id == user.id:
            return 'Error: Invalid id'

        if target_id == user.player.last_attacked:
            return 'Error: Cant attack same player twice !'

        attacking_pigeons = Pigeon.objects.filter(player_id=user.id, is_attacker=True)
        defending_pigeons = Pigeon.objects.filter(player_id=target_id, defender_pos__isnull=False)

        if len(attacking_pigeons) != 5:
            return 'Error: You need 5 pigeons to attack'

        user.player.attacking_id = target_id
        user.player.save()

    return list(attacking_pigeons.values()), list(defending_pigeons.values())
