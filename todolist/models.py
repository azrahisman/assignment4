from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField()