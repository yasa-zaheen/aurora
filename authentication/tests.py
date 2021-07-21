from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.shortcuts import reverse

# Create your tests here.


class SignInTests(TestCase):

    def test_incorrect_username(self):

        User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testuser"
        )

        client = Client()

        response = client.post(reverse("authentication:sign_in"), {
            "username": "testuser2",
            "password": "testuser",
        })

        self.assertEqual(response.status_code, 401)

    def test_incorrect_password(self):

        User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testuser"
        )

        client = Client()

        response = client.post(reverse("authentication:sign_in"), {
            "username": "testuser",
            "password": "testuser2",
        })

        self.assertEqual(response.status_code, 401)

    def test_user_in_anonymous(self):

        User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testuser"
        )

        client = Client()

        client.login(username="testuser", password="testuser")

        response = client.get(reverse("authentication:sign_in"))

        self.assertEqual(response.status_code, 301)


class SignUpTests(TestCase):

    def test_account_with_username_exists(self):

        User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testuser"
        )

        client = Client()

        response = client.post(reverse("authentication:sign_up"), {
            "username": "testuser",
            "email": "testuser2@gmail.com",
            "password": "testuser",
        })

        self.assertEqual(response.status_code, 409)

    def test_account_with_email_exists(self):

        User.objects.create_user(
            username="testuser2",
            email="testuser@gmail.com",
            password="testuser"
        )

        client = Client()

        response = client.post(reverse("authentication:sign_up"), {
            "username": "testuser2",
            "email": "testuser@gmail.com",
            "password": "testuser",
        })

        self.assertEqual(response.status_code, 409)

    def test_password_less_than_eight_characters(self):

        User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testuser"
        )

        client = Client()

        response = client.post(reverse("authentication:sign_up"), {
            "username": "testuser2",
            "email": "testuser2@gmail.com",
            "password": "testus",
        })

        self.assertEqual(response.status_code, 406)


class SignOutTests(TestCase):

    def test_user_is_anonymous(self):

        client = Client()

        response = client.get(reverse("authentication:sign_out"))

        self.assertEqual(response.status_code, 301)
