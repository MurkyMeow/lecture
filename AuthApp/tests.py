from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

class AccountTests(APITestCase):
    def setUp(self):
        User.objects.create(
            username='Apps', email='h@gmail.com', password='blabla123'
        )

    def test_create_account(self):
        res = self.client.post('/auth/signup/', {
            'name': 'RulonOboev',
            'email': 'fuckyouhoney@gmail.com',
            'password': 'getoverhere',
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_login(self):
        res = self.client.post('/auth/signin/', {
            'email': 'h@gmail.com',
            'password': 'blabla123',
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
