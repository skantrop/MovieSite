from django.contrib.auth.views import LogoutView
from django.urls import path

from account.views import *

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='registration'),
    path('success_registration/', SuccessfulRegistrationView.as_view(), name='successful-registration'),
    path('activation/', ActivationView.as_view(), name='activation'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path('change_password/', ChangePasswordView.as_view(), name='change-password'),
    path('forgot_password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('forgot_pass_complete/', TemplateView.as_view(template_name='account/forgot_pass_complete.html'),
         name='forgot-pass-complete'),
    path('profile/', profile, name='profile'),

]