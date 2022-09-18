from django.db.models import Sum
from ..models import Pigeon
from datetime import datetime, timezone
from django.db import transaction
from ..models import TR_Lvl_info
from ..models import Player
import math
import logging


def update_user_values(user):
    """
    update player droppings and seeds
    """
    with transaction.atomic():
        drop_min = (
            Pigeon.objects.filter(player__user=user.id, is_open=True, is_sold=False)
            .aggregate(tot_drop=Sum("droppings_minute"))
            .get("tot_drop")
            or 0
        )

        delta_time = datetime.now(timezone.utc) - user.player.last_updated_at
        delta_minutes = delta_time.total_seconds() / 60

        droppings_in_delta_time = round(delta_minutes * drop_min)
        lvl_info = TR_Lvl_info.objects.get(lvl=user.player.lvl)
        seeds_in_delta_time = round(delta_minutes * lvl_info.seeds_minute)

        # droppings
        if user.player.droppings != lvl_info.max_droppings:
            droppings_to_apply = user.player.droppings + droppings_in_delta_time
            user.player.droppings = min(droppings_to_apply, lvl_info.max_droppings)

        # seeds
        if user.player.seeds != lvl_info.max_seeds:
            seeds_to_apply = user.player.seeds + seeds_in_delta_time
            user.player.seeds = min(seeds_to_apply, lvl_info.max_seeds)

        user.player.last_updated_at = datetime.now(timezone.utc)
        user.player.save()
