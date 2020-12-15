from django.db import models

class TR_Lvl_info(models.Model):
    lvl = models.IntegerField(default=1, db_index=True) #index db
    max_seeds = models.IntegerField(default=0)
    max_droppings = models.IntegerField(default=0)
    max_feathers = models.IntegerField(default=0)

    