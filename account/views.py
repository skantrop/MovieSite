from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from account.forms import RegistrationForm
from account.models import User


class RegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'account/registration.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    success_message = 'Your account is successfully registered'


class SignInView(LoginView):
    template_name = 'account/login.html'
    success_url = reverse_lazy('home')




class ProfileView(DetailView):
    model = User
    template_name = 'account/profile.html'

# def profile(request):
#     return render(request, 'account/profile.html')