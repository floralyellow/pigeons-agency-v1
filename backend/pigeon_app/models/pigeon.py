from django.db import models
from .player import Player

class Pigeon(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    p_type = models.IntegerField(default=1)
    name = models.CharField(max_length=30, default="test")
    element = models.IntegerField(default=1)
    attack = models.IntegerField(default=1)
    defense = models.IntegerField(default=1)
    shield = models.IntegerField(default=0)
    speed = models.IntegerField(default=1)
    droppings_minute = models.IntegerField(default=1)
    feathers = models.IntegerField(default=1)
    creation_time = models.DateTimeField(auto_now_add=True, null=True)
    active_time = models.DateTimeField(auto_now_add=True, null=True)
    is_open = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    is_attacker = models.BooleanField(default=False)
    is_defender = models.BooleanField(default=False)


