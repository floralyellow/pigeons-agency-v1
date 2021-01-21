from django.db import models

class TR_Expedition(models.Model):
    lvl = models.IntegerField(default=1, db_index=True) #index db
    seeds = models.IntegerField(default=0)
    duration = models.IntegerField(default=0)
    name = models.CharField(max_length=30, default="test")
    
    