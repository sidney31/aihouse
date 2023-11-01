from django.db import models
from django.shortcuts import render
from django.contrib.auth.models import AbstractUser
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.models import Page
from wagtail.fields import RichTextField, StreamField
from wagtail.admin.panels import FieldPanel


class User(AbstractUser):
    pass

class UsersPage(RoutablePageMixin, Page):
    @route(r'^login/')
    def login_page(self, request):
        context = self.get_context(request)
        return render(request, 'users/login.html', context)
    

    header = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel('header'),
    ]