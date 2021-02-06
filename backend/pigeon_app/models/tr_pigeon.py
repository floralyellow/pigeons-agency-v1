from django.db import models
from django.contrib.postgres.fields import ArrayField


# Reference table used to generate a random pigeon when expedition is launched
class TR_Pigeon(models.Model):
    lvl_expedition = models.IntegerField(default=1)
    coef_chance_rate = models.IntegerField(default=1)
    pigeon_type = models.IntegerField(default=1)
    pigeon_id = models.IntegerField(default=1)
    src = models.CharField(max_length=30, default="test.png")
    name = models.CharField(max_length=30, default="test")
    min_atk = models.IntegerField(default=1)
    max_atk = models.IntegerField(default=1)
    min_life = models.IntegerField(default=1)
    max_life = models.IntegerField(default=1)
    min_shield = models.IntegerField(default=1)
    max_shield = models.IntegerField(default=1)
    speed = models.IntegerField(default=1)
    min_luck_1 = models.IntegerField(default=1)
    effect_1_chance = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    effect_1 = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    min_luck_2 = models.IntegerField(default=1)
    effect_2_chance = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    effect_2 = ArrayField(models.IntegerField(null=True, blank=True), null=True, blank=True)
    is_active = models.BooleanField(default=True)


