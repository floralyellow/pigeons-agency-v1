from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=30)
    feathers = models.IntegerField()