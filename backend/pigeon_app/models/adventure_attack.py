from django.db import models
from rest_framework import serializers

from .abstract_attack import AbstractAttack
from .adventure import Adventure


class AdventureAttack(AbstractAttack):
    adventure = models.ForeignKey(
        Adventure, on_delete=models.CASCADE, related_name="linked_adventure"
    )
    is_victory = models.BooleanField(default=False)


class AdventureAttackSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdventureAttack
        fields = "__all__"
