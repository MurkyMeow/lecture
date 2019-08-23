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
        self.comments = [
            Comment.objects.create(user=u, lecture_id=1, slide_id=1, text='foo'),
            Comment.objects.create(user=u, lecture_id=1, slide_id=1, text='bar'),
        ]
        self.client.force_authenticate(u)

    def test_get_comments(self):
        params = { 'lecture_id': 1, 'slide_id': 1 }
        res = self.client.get('/course/comments/', params)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(self.comments))

    def test_create_comment(self):
        comment = { 'lecture_id': 2, 'slide_id': 1, 'text': 'qwerqwer' }
        res = self.client.post('/course/comments/', comment)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['text'], comment['text'])
        self.assertEqual(res.data['slide_id'], comment['slide_id'])
        self.assertEqual(res.data['lecture_id'], comment['lecture_id'])

