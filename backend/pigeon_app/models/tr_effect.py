from django.db import models

# Reference table used to assign effects to pigeons when generated
class TR_Effect(models.Model):
    lvl_expedition = models.IntegerField(default=1)
    coef_chance_rate = models.IntegerField(default=1)
    p_type = models.IntegerField(default=1)
    p_id = models.IntegerField(default=1)
    effect_id = models.IntegerField(default=1)
    has_effect_value = models.BooleanField(default=True)
    min_effect_value = models.IntegerField(default=1)
    max_effect_value = models.IntegerField(default=1)
    effect_name = models.CharField(max_length=30, default="test")
    effect_desc = models.CharField(max_length=50, default="test")



