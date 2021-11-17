from django.db import models

class TR_Expedition(models.Model):
    lvl = models.IntegerField(default=1, db_index=True) #index db
    expedition_type = models.IntegerField(default=0)
    seeds = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default="test")
    min_drop_minute = models.IntegerField(default=0)
    max_drop_minute = models.IntegerField(default=0)
    min_feathers = models.IntegerField(default=0)
    max_feathers = models.IntegerField(default=0)

    