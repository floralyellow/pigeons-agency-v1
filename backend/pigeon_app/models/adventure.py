from django.db import models
from .player import Player
from rest_framework import serializers


class Adventure(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    lvl = models.IntegerField(default=0)
    encounter = models.IntegerField(default=0)
    nb_tries = models.IntegerField(default=0)
    is_success = models.BooleanField(default=False)
    reward_droppings = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    completed_at =  models.DateTimeField(null=True)

class AdventureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adventure
        fields = '__all__'