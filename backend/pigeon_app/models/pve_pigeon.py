from django.db import models
from rest_framework import serializers

from .abstract_pigeon import AbstractPigeon


class PvePigeon(AbstractPigeon):
    player_id = models.IntegerField(default=-1)



class PvePigeonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PvePigeon
        fields = "__all__"
