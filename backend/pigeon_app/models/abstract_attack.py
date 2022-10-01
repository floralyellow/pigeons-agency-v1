from django.db import models

from .player import Player


class AbstractAttack(models.Model):
    attacker = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="%(class)s_player_atk"
    )
    atk_tot_score = models.IntegerField(default=0)
    atk_tot_phys = models.IntegerField(default=0)
    atk_tot_magic = models.IntegerField(default=0)
    atk_tot_shield = models.IntegerField(default=0)
    def_tot_score = models.IntegerField(default=0)
    def_tot_phys = models.IntegerField(default=0)
    def_tot_magic = models.IntegerField(default=0)
    def_tot_shield = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True
