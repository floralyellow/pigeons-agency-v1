from django.db import models
from rest_framework import serializers

from .abstract_pigeon import AbstractPigeon
from .player import Player


class Pigeon(AbstractPigeon):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)


class PigeonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pigeon
        fields = "__all__"
