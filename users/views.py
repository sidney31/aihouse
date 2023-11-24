from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login

from .forms import UserRegistrationForm, UserAuthenticationForm
from .models import User


@login_required(login_url='users:login')
def profile_view(request):
    return render(request, 'users/profile.html')


class RegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginView(FormView):
    form_class = UserAuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        login(self.request, User)
        return super().form_valid(form)
