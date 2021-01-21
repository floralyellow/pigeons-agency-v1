from ..models import Pigeon
from datetime import datetime,timezone
from ..models import TR_Lvl_info
from ..models import Player
import math

def update_droppings(user):
        """
        update player droppings
        """
        pigeons = Pigeon.objects.filter(player__user = user.id)
        player_droppings_minute = sum(pigeon.droppings_minute for pigeon in pigeons)
        # print("player_dropping_minute : "+str(player_droppings_minute)) 
        delta_time = datetime.now(timezone.utc) - user.player.last_updated_at
        delta_minutes = delta_time.total_seconds() / 60
        # print("delta_minute: "+str(delta_minutes))
        droppings_in_delta_time = math.ceil(delta_minutes * player_droppings_minute)
        # print("droppings_in_delta"+str((droppings_in_delta_time)))
        player_lvl = Player.objects.get(user = user.id).lvl
        max_droppings = TR_Lvl_info.objects.get(lvl=player_lvl).max_droppings
        
        # petite optimisation bien pensé ne pas remplacer par  player.user.droppings +  droppings_in_delta_time < max_droppings
        if user.player.droppings < max_droppings:
            droppings_to_apply = user.player.droppings +  droppings_in_delta_time
            user.player.droppings = min(droppings_to_apply,max_droppings)
        # print(user.player.droppings)
        user.player.save()

def update_all_player_values(user):
    '''update User values (seeds droppins)'''
    update_droppings(user)
    
    pass