from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User

user = {
    'name': 'Test',
    'email': 'test@test.com',
    'password': 'testtest123'
}

class AccountTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username=user['name'], email=user['email'], password=user['password']
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
            'email': user['email'],
            'password': user['password'],
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_signup_name_conflict(self):
        name = self.client.post('/auth/signup/', {
            'name': user['name'], 'email': 'z', 'password': 'z',
        })
        self.assertEqual(name.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(name.data['name'], True)

    def test_signup_email_conflict(self):
        email = self.client.post('/auth/signup/', {
            'email': user['email'], 'name': 'z', 'password': 'z',
        })
        self.assertEqual(email.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(email.data['email'], True)