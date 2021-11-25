from ..models import attack
from ..models import TR_Lvl_info
from ..models import TR_Expedition
from ..models import Attack
from ..models import AttackPigeon
from django.contrib.auth.models import User
from ..models import Player, Pigeon
from pigeon_app.models.player import UserSerializer
from django.db import transaction
from datetime import datetime,timezone,timedelta
import random
import logging

def attack_player(user, target_id):
    SECONDS_NEXT_ATTACK = 2 * 60 # 2 minutes

    with transaction.atomic():
        target = Player.objects.filter(id=target_id)

        if len(target) != 1 or target_id == user.id:
            return 'Error: Invalid id'

        if target_id == user.player.last_attacked:
            return 'Error: Cant attack same player twice !'
        
        logging.debug(str(user.player.time_last_attack))
        logging.debug(str(SECONDS_NEXT_ATTACK))
        logging.debug(str(datetime.now(timezone.utc)))

        if user.player.time_last_attack + timedelta(seconds=SECONDS_NEXT_ATTACK) > datetime.now(timezone.utc):
            return 'Error: Cant attack yet !'


        attacking_pigeons = Pigeon.objects.filter(player_id=user.id, is_in_team=True)
        defending_pigeons = Pigeon.objects.filter(player_id=target_id, is_in_team=True)

        # if len(attacking_pigeons) != 5:
        #     return 'Error: You need 5 pigeons to attack'
        total_phys_atk = 0
        total_phys_def = 0
        total_magic_atk = 0
        total_magic_def = 0
        total_shield_atk = 0
        total_shield_def = 0
        # sum shields needed before loop
        sum_shield_value_atk = sum([i.shield for i in attacking_pigeons]) 
        sum_shield_value_def = sum([i.shield for i in attacking_pigeons])

        current_attack = Attack(attacker=user.player, defender=target[0])
        current_attack.save()

        for p in attacking_pigeons:
            bonus_phys_atk = round(random.randint(-15,15) * p.phys_atk / 100)
            bonus_magic_atk = round(random.randint(-15,15) * p.magic_atk / 100)

            if p.phys_atk > 0:
                total_phys_atk += p.phys_atk + bonus_phys_atk
                total_shield_def += sum_shield_value_def

            total_magic_atk += p.magic_atk + bonus_magic_atk

            attack_pigeon = AttackPigeon(attack=current_attack,pigeon=p,is_attacker=True,phys_atk_bonus=bonus_phys_atk,magic_atk_bonus=bonus_magic_atk)
            attack_pigeon.save()

        for p in defending_pigeons:
            bonus_phys_atk = round(random.randint(-15,15) * p.phys_atk / 100)
            bonus_magic_atk = round(random.randint(-15,15) * p.magic_atk / 100)

            if p.phys_atk > 0:
                total_phys_def += p.phys_atk + bonus_phys_atk
                total_shield_atk += sum_shield_value_atk

            total_magic_def += + p.magic_atk + bonus_magic_atk

            attack_pigeon = AttackPigeon(attack=current_attack,pigeon=p,is_attacker=False,phys_atk_bonus=bonus_phys_atk,magic_atk_bonus=bonus_magic_atk)
            attack_pigeon.save()

        total_attacker = total_phys_atk + total_magic_atk - total_shield_def
        total_defender = total_phys_def + total_magic_def - total_shield_atk
        
        winner_id = user.id if total_attacker > total_defender else target_id

        # TODO stolen droppings

        # TODO militaryscore

        # TODO timetonextattack & last attack id

        # TODO protecteduntil (with model)

        current_attack.winner_id=winner_id
        current_attack.atk_tot_score=total_attacker
        current_attack.atk_tot_phys=total_phys_atk
        current_attack.atk_tot_magic=total_magic_atk
        current_attack.atk_tot_shield=total_shield_atk
        current_attack.def_tot_score=total_defender
        current_attack.def_tot_phys=total_phys_def
        current_attack.def_tot_magic=total_magic_def
        current_attack.def_tot_shield=total_shield_def
        current_attack.stolen_droppings=0
        current_attack.atk_old_military_score=0
        current_attack.atk_new_military_score=0
        current_attack.def_old_military_score=0
        current_attack.def_new_military_score=0
        current_attack.save()

    return list(attacking_pigeons.values()), list(defending_pigeons.values())
