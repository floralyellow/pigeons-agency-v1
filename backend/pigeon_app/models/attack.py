from django.db import models
from rest_framework import serializers

from .abstract_attack import AbstractAttack
from .player import Player


class Attack(AbstractAttack):
    defender = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="player_def")
    winner_id = models.IntegerField(default=0)
    stolen_droppings = models.IntegerField(default=0)
    atk_old_military_score = models.IntegerField(default=0)
    atk_new_military_score = models.IntegerField(default=0)
    def_old_military_score = models.IntegerField(default=0)
    def_new_military_score = models.IntegerField(default=0)


class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = "__all__"
