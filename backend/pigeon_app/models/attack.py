from django.db import models
from .player import Player
from rest_framework import serializers


class Attack(models.Model):
    attacker = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_atk')
    defender = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='player_def')
    winner_id = models.IntegerField(default=0)
    atk_tot_score = models.IntegerField(default=0)
    atk_tot_phys = models.IntegerField(default=0)
    atk_tot_magic = models.IntegerField(default=0)
    atk_tot_shield = models.IntegerField(default=0)
    def_tot_score = models.IntegerField(default=0)
    def_tot_phys = models.IntegerField(default=0)
    def_tot_magic = models.IntegerField(default=0)
    def_tot_shield = models.IntegerField(default=0)
    stolen_droppings = models.IntegerField(default=0)
    atk_old_military_score = models.IntegerField(default=0)
    atk_new_military_score = models.IntegerField(default=0)
    def_old_military_score = models.IntegerField(default=0)
    def_new_military_score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


class AttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attack
        fields = '__all__'