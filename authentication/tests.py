from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.shortcuts import reverse

# Create your tests here.


class SignInTests(TestCase):

    def test_incorrect_password(self):

        client = Client()

        response = client.post(reverse("authentication:sign_in"), {
            "username": "yasa.zaheen",
            "password": "anonymous"
        })

        self.assertEqual(response.status_code, 403)

    def test_user_does_not_exist(self):

        client = Client()

        response = client.post(reverse("authentication:sign_in"), {
            "username": "yasazaheen",
            "password": "anonymous"
        })

        self.assertEqual(response.status_code, 403)
