from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth.hashers import make_password


class Player(models.Model):
    lvl = models.IntegerField(default=1)
    seeds = models.IntegerField(default=0)
    droppings = models.IntegerField(default=0)
    feathers = models.IntegerField(default=0)
    military_score = models.IntegerField(default=0)
    last_attacked = models.IntegerField(default=-1)
    time_last_attack = models.DateTimeField(auto_now_add=True, null=True)
    last_connected_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['lvl', 'seeds', 'droppings', 'feathers', 'military_score', 'last_attacked', 'time_last_attack']


class UserSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(many=False, read_only=True)
    password = serializers.CharField(required=True,write_only=True) #par défaut parole de gugu django il utilise les post du user sans mdp

    class Meta:
        model = User
        fields = ['id', 'username','player','password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)
        
