from django.db import models

# Reference table used to assign effects to pigeons when generated
class TR_Effect(models.Model):
    effect_id = models.IntegerField(default=1, db_index=True) #index db
    effect_name = models.CharField(max_length=30, default="test")
    is_active_effect = models.BooleanField(default=True)
    has_value = models.BooleanField(default=True)
    min_value = models.IntegerField(default=1)
    max_value = models.IntegerField(default=1)
    desc = models.CharField(max_length=50, default="test")



