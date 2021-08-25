from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils.crypto import get_random_string

from movies.celery import app

User = get_user_model()

@app.task
def send_activation_mail(email, activation_code):
    message = f'http://127.0.0.1:8000/accounts/activation/?u={activation_code}'
    send_mail('Account activation', message, 'test@gmail.com', [email])

@app.task
def send_password(email, new_pass):
    send_mail('Восстановление пароля', f'Ваш новый пароль: {new_pass}', 'test@gmail.com', [email])

@app.task
def send_new_addition_mail(email, title):
    message = f"We've added new movie {title}, watch it and enjoy"
    send_mail('Активация аккаунта', message, 'test@gmail.com', [email])

