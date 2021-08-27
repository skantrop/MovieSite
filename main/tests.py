from django.test import TestCase

from django.test import TestCase
from django.urls import reverse


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('registration')
        self.user = {
            'email': 'test@email.com',
            'password': 'password',
            'password_confirm': 'password_confirm',
        }

        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_user_register(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/registration.html')


from django.test import Client
csrf_client = Client(enforce_csrf_checks=True)


