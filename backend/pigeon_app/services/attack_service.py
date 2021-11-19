from ..models import TR_Lvl_info
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

def attack_player(user, pigeon_ids):

    with transaction.atomic():
        atk_pigeons = Pigeon.objects.filter(player_id=user.id, is_sold=False, is_open=True, is_attacker=True)
        logging.info(atk_pigeons.values_list('id',flat=True))

        if not all(int(p) in atk_pigeons.values_list('id',flat=True) for p in pigeon_ids): 
            return 'Error: wrong id'

        def_pigeons = Pigeon.objects.filter(player_id=user.player.attacking_id, is_sold=False, is_open=True, defender_pos__isnull=False)
        logging.info(def_pigeons)


    return 'wip'

