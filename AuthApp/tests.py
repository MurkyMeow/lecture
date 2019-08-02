from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
# Create your tests here.


class AccountTests(APITestCase):
    def setUp(self):
        User.objects.create(username='DabApps',
                            email='hello@gmail.com', password='blablabla123')

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = '/auth/signup/'
        data = {'name': 'RulonOboev', 'email': 'fuckyouhoney@gmail.com',
                'password': 'getoverhere'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_account(self):
        """
        Ensure we can login to new account object.
        """
        url = '/auth/signin/'
        data = {'email': 'hello@gmail.com', 'password': 'blablabla123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
