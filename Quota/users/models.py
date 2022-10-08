from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    user1 = User.objects.create(username="Earth",password="Ironman1234")