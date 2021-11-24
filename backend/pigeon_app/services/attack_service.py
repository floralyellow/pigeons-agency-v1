from ..models import TR_Lvl_info
from ..models import TR_Expedition
from django.contrib.auth.models import User
from ..models import Player, Pigeon
from pigeon_app.models.player import UserSerializer
from django.db import transaction
from datetime import datetime,timezone
import random
import logging

def attack_player(user, target_id):
    SECONDS_NEXT_ATTACK = 2 * 60 # 2 minutes

    with transaction.atomic():
        res = Player.objects.filter(id=target_id)

        if len(res) != 1 or target_id == user.id:
            return 'Error: Invalid id'

        if target_id == user.player.last_attacked:
            return 'Error: Cant attack same player twice !'
        
        logging.debug(str(user.player.time_last_attack))
        logging.debug(str(SECONDS_NEXT_ATTACK))
        logging.debug(str(datetime.now(timezone.utc)))
        logging.debug(str(user.player.time_last_attack + SECONDS_NEXT_ATTACK))

        if user.player.time_last_attack + SECONDS_NEXT_ATTACK > datetime.now(timezone.utc):
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

        for p in attacking_pigeons:
            bonus_phys_atk = round(random.randint(-15,15) * p.phys_atk / 100)
            bonus_magic_atk = round(random.randint(-15,15) * p.magic_atk / 100)
            total_phys_atk = total_phys_atk + p.phys_atk + bonus_phys_atk
            total_magic_atk = total_magic_atk + p.magic_atk + bonus_magic_atk
            total_shield_atk = total_shield_atk + p.shield




        shield_attackers = sum([i.shield for i in attacking_pigeons])
        shield_defenders = sum([i.shield for i in defending_pigeons])

        print(shield_attackers)

        phys_atk_attackers=sum([max(i.phys_atk - shield_defenders,0) for i in attacking_pigeons])
        phys_atk_defenders=sum([max(i.phys_atk - shield_attackers,0) for i in defending_pigeons])

        # print('atk1 : '+str(atk1))
        # print('atk2 : '+str(atk2))

        magic_atk_attackers=sum([i.magic_atk  for i in attacking_pigeons])
        magic_atk_defenders=sum([i.magic_atk  for i in defending_pigeons])

        tot1 = atk1+mgc1
        tot2 = atk2+mgc2
        # print('mgc1 : '+str(mgc1))
        # print('mgc2 : '+str(mgc2))

        #print('tot : '+str(atk1+mgc1) +  ' -- '+str(atk2+mgc2))

        return tot1 > tot2, tot1 == tot2, tot1 < tot2, round(((tot1 - tot2) * 2.0 / (tot1+tot2)),2)






        user.player.last_attacked = target_id
        user.player.time_last_attack = datetime.now(timezone.utc)
        user.player.save()

    return list(attacking_pigeons.values()), list(defending_pigeons.values())

# def attack_player(user, pigeon_ids):

#     with transaction.atomic():
#         atk_pigeons = Pigeon.objects.filter(player_id=user.id, is_sold=False, is_open=True, is_attacker=True)
#         logging.info(atk_pigeons.values_list('id',flat=True))

#         if not all(int(p) in atk_pigeons.values_list('id',flat=True) for p in pigeon_ids): 
#             return 'Error: wrong id'

#         def_pigeons = Pigeon.objects.filter(player_id=user.player.attacking_id, is_sold=False, is_open=True, defender_pos__isnull=False)
#         logging.info(def_pigeons)


#     return 'wip'

