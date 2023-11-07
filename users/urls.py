from django.urls import path, include
from users import views
from .views import RegistrationView, LoginView
from django.contrib.auth import urls as djangoauth_urls


app_name = 'users'

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
    path('/', include(djangoauth_urls)),
]
