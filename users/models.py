from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phoneNumber = PhoneNumberField()
    models.EmailField(max_length=254, null=False, blank=False, unique=False)
    phone = PhoneNumberField(null=False, blank=False, unique=False)
