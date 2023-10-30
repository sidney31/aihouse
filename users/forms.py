from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('phoneNumber', 'email', 'password',)