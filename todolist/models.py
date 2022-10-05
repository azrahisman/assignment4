from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=128, blank = True)

class ItemTodolist(models.Model):
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField()

user1 = User.objects.create(name="Azra", email="azra.batrisyia11@ui.ac.id", pk=1)
ItemTodolist.objects.update(user=user1)