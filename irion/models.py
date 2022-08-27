from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    id = models.CharField(max_length=15, unique=True, default='', primary_key=True)
    nickname = models.CharField(max_length=15, unique=True, default='')
    birth = models.DateField()

    def __str__(self):
        return self.username