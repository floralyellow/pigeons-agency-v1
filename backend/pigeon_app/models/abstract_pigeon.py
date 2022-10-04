from django.db import models


class AbstractPigeon(models.Model):
    pigeon_type = models.IntegerField(default=1)
    name = models.CharField(max_length=30, default="test")
    src = models.CharField(max_length=30, default="test")
    pigeon_id = models.IntegerField(default=1)
    lvl = models.IntegerField(default=1)
    luck = models.IntegerField(default=1)
    phys_atk = models.IntegerField(default=1)
    magic_atk = models.IntegerField(default=1)
    shield = models.IntegerField(default=0)
    droppings_minute = models.IntegerField(default=1)
    feathers = models.IntegerField(default=1)
    creation_time = models.DateTimeField(null=True)
    active_time = models.DateTimeField(null=True)
    is_open = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    is_in_team_A = models.BooleanField(default=False)
    is_in_team_B = models.BooleanField(default=False)

    class Meta:
        abstract = True
