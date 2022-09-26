from django.contrib.postgres.fields import ArrayField
from django.db import models


# Reference table used to generate a random pigeon when expedition is launched
class TR_Pigeon(models.Model):
    lvl_expedition = models.IntegerField(default=1, db_index=True)  # index db
    pigeon_type = models.IntegerField(default=1)
    pigeon_id = models.IntegerField(default=1)
    name = ArrayField(models.CharField(max_length=30), null=True, blank=True)
    src = ArrayField(models.CharField(max_length=30), null=True, blank=True)
    min_phys_atk = models.IntegerField(default=1)
    max_phys_atk = models.IntegerField(default=1)
    min_magic_atk = models.IntegerField(default=1)
    max_magic_atk = models.IntegerField(default=1)
    min_shield = models.IntegerField(default=1)
    max_shield = models.IntegerField(default=1)
