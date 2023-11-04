from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm

from django.contrib import auth
from django.urls import reverse


def profile_view(request):
    return render(request, 'users/profile.html')