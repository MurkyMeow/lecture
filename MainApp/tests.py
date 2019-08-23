from rest_framework.test import APITestCase
from rest_framework import status
from .models import Comment
from django.contrib.auth.models import User

user = {
    'name': 'Test',
    'email': 'test@test.com',
    'password': 'testtest123'
}

class CommentsTests(APITestCase):
    def setUp(self):
        u = User.objects.create(
            username=user['name'], email=user['email'], password=user['password']
        )
        self.client.force_authenticate(u)

    def test_create_comment(self):
        comment = { 'lectureID': 2, 'slideID': 1, 'text': 'qwerqwer' }
        res = self.client.post('/course/comments/', comment)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

