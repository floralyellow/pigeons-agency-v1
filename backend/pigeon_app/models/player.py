from django.db import models

class Player(models.Model):
    username = models.CharField(max_length=30, default="test")
    lvl = models.IntegerField(default=1)
    seeds = models.IntegerField(default=0)
    droppings = models.IntegerField(default=0)
    feathers = models.IntegerField(default=0)
    military_score = models.IntegerField(default=0)
    
    last_connected_at = models.DateTimeField(auto_now_add=True, null=True)
    last_updated_at = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

