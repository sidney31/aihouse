from django import forms
from users.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+79999999999',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
    }))
    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '+7(___)___-__-__',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Повторите ввод пароля',
    }))
class Meta:
    model = User
    fields = ('number', 'email', 'password1', 'password2')