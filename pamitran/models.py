from django.db import models
from django.contrib.auth.models import User

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comments = models.CharField(max_length=300, blank=True)