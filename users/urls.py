from django.urls import path
from users import views
from .views import RegistrationView


app_name = 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('registration/', RegistrationView.as_view(), name='registration')
]
