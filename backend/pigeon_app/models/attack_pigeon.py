from django.db import models
from .attack import Attack
from .pigeon import Pigeon, PigeonSerializer
from rest_framework import serializers


class AttackPigeon(models.Model):
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE)
    pigeon = models.ForeignKey(Pigeon, on_delete=models.CASCADE)
    is_attacker = models.BooleanField(default=False)
    phys_atk_bonus = models.IntegerField(default=0)
    magic_atk_bonus = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class AttackPigeonSerializer(serializers.ModelSerializer):
    pigeon = PigeonSerializer(many=False, read_only=True)

    class Meta:
        model = AttackPigeon
        fields = ['id', 'pigeon','is_attacker','phys_atk_bonus','magic_atk_bonus']