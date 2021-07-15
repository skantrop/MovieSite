from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import *

urlpatterns = [
    path('sign-up/', RegistrationView.as_view(), name='registration'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-profile/', ProfileView.as_view(), name='profile'),
]