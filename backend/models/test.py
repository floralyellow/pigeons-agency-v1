from django.db import models

class Test(models.Model):
    value = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)