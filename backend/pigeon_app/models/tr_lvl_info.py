from django.db import models


class TR_Lvl_info(models.Model):
    lvl = models.IntegerField(default=1, db_index=True)  # index db
    seeds_minute = models.IntegerField(default=0)
    max_seeds = models.IntegerField(default=0)
    max_droppings = models.IntegerField(default=0)
    max_feathers = models.IntegerField(default=0)
    max_pigeons = models.IntegerField(default=10)
