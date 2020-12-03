from django.db import models
from .player import Player

class Pigeon(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    p_type = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
