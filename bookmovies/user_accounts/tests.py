from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import CustomUser
from rest_framework.authtoken.models import Token

class SignUpAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.signup_url = reverse('signup')

    def test_signup_success(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword',
            'phone_number': '1234567890'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_signup_failure(self):
        # Test case for invalid data
        data = {
            'username': '',
            'password': 'testpassword',
            'phone_number': '1234567890'
        }
        response = self.client.post(self.signup_url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(CustomUser.objects.count(), 0)

class LogoutAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.logout_url = reverse('logout')

    def test_logout_success(self):
        # Create a user and obtain a token
        user = CustomUser.objects.create_user(username='testuser', password='testpassword')
        token = Token.objects.create(user=user)

        # Set the token in the authorization header
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        # Send the logout request
        response = self.client.post(self.logout_url)

        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertFalse(Token.objects.filter(user=user).exists())

    def test_logout_failure(self):
        # Send the logout request without a token
        response = self.client.post(self.logout_url)

        # Verify the response
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
