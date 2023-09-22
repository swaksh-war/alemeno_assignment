from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255, default='Null')
    password = models.CharField(max_length=255, default='Null')
    email = models.CharField(max_length=255, default='Null')

    def __str__(self):
        return self.username



