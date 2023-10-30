from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phoneNumber = models.IntegerField()
    email = models.EmailField(max_length=254, null=False, blank=False, unique=False)
    password = models.TextField(max_length=64, null=False, blank=False, unique=False)