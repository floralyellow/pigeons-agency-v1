from django.db import models
from .player import Player
from rest_framework import serializers


class Pigeon(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    pigeon_type = models.IntegerField(default=1)
    name = models.CharField(max_length=30, default="test")
    pigeon_id = models.IntegerField(default=1)
    luck = models.IntegerField(default=1)
    element = models.IntegerField(default=1) # Mountain Forest Beach
    attack = models.IntegerField(default=1)
    life = models.IntegerField(default=1)
    shield = models.IntegerField(default=0)
    speed = models.IntegerField(default=1)
    droppings_minute = models.IntegerField(default=1)
    feathers = models.IntegerField(default=1)
    creation_time = models.DateTimeField(null=True)
    active_time = models.DateTimeField(null=True)
    effect_1_id = models.IntegerField(default=1)
    effect_2_id = models.IntegerField(default=1)
    effect_1_value = models.IntegerField(default=1)
    effect_2_value = models.IntegerField(default=1)
    is_open = models.BooleanField(default=False)
    is_sold = models.BooleanField(default=False)
    is_attacker = models.BooleanField(default=False)
    defender_pos = models.IntegerField(null=True)


class PigeonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pigeon
        fields = '__all__'