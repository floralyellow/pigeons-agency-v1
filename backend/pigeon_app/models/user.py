from django.contrib.auth.models import AbstractUser
from .player import Player
from django.db import models

from backend.pigeon_app.models.player import player


class UserSerializer(serializers.ModelSerializer):
    player = serializers.PrimaryKeyRelatedField(many=False, queryset=Player.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']