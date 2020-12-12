from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers


class Player(models.Model):
    lvl = models.IntegerField(default=1)
    seeds = models.IntegerField(default=0)
    droppings = models.IntegerField(default=0)
    feathers = models.IntegerField(default=0)
    military_score = models.IntegerField(default=0)
    last_connected_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    feathers = models.IntegerField(default=0)
    

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(many=False, read_only=True)
    password = serializers.CharField(required=True,write_only=True) #par défaut parole de gugu django il utilise les post du user sans mdp ce fdp

    class Meta:
        model = User
        fields = ['id', 'username','player','password']
        
