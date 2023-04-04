from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .common.utils import generate_token


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_token = generate_token()
        self.invalid_token = 'invalid_token'

    def test_generate_token(self):
        response = self.client.post(reverse('token-generate'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

    def test_validate_token(self):
        # Test with a valid token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.valid_token)
        response = self.client.post(reverse('token-validate'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test with an invalid token
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.invalid_token)
        response = self.client.post(reverse('token-validate'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
