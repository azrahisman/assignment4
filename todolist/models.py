from django.db import models
from django.contrib.auth.models import User
from django import forms

class Task(models.Model):
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField()

