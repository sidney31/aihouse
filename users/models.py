from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel


class User(AbstractUser):
    pass
