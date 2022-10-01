from django.db import models
from rest_framework import serializers

from .player import Player
from .abstract_pigeon import AbstractPigeon


class Pigeon(AbstractPigeon):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)


class PigeonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pigeon
        fields = "__all__"
