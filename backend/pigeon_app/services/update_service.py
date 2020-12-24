from ..models import Pigeon
from datetime import datetime,timezone
from ..models import TR_Lvl_info
from ..models import Player
import math

def update_user_values(user):
        """
        update player droppings
        """
        drop_min = Pigeon.objects.filter(player__user = user.id, is_open = True, is_sold=False).aggregate(tot_drop=Sum('droppings_minute')).tot_drop
        # player_droppings_minute = sum(pigeon.droppings_minute for pigeon in pigeons)
        print("player_dropping_minute : "+str(drop_min)) 
        delta_time = datetime.now(timezone.utc) - user.player.last_updated_at
        delta_minutes = delta_time.total_seconds() / 60
        # print("delta_minute: "+str(delta_minutes))
        droppings_in_delta_time = math.ceil(delta_minutes * drop_min)
        # print("droppings_in_delta"+str((droppings_in_delta_time)))
        # player_lvl = Player.objects.get(user = user.id).lvl
        lvl_info = TR_Lvl_info.objects.get(lvl=player_lvl)#.max_droppings
        seeds_in_delta_time = math.ceil(delta_minutes * lvl_info.seeds_minute)
        
        # droppings
        if user.player.droppings < lvl_info.max_droppings:
            droppings_to_apply = user.player.droppings +  droppings_in_delta_time
            user.player.droppings = min(droppings_to_apply, lvl_info.max_droppings)

        if user.player.seeds < lvl_info.max_seeds:
            seeds_to_apply = user.player.seeds + seeds_in_delta_time
            user.player.droppings = min(seeds_to_apply,lvl_info.max_seeds)
        # print(user.player.droppings)
        user.player.save()
