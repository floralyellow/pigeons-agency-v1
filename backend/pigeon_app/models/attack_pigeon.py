from django.db import models
from .attack import Attack
from .pigeon import Pigeon
from rest_framework import serializers


class AttackPigeon(models.Model):
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE)
    pigeon = models.ForeignKey(Pigeon, on_delete=models.CASCADE)
    is_attacker = models.BooleanField(default=False)
    phys_atk_bonus = models.IntegerField(default=0)
    magic_atk_bonus = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class AttackPigeonSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttackPigeon
        fields = '__all__'