from rest_framework.test import APITestCase
from rest_framework import status
from .models import Comment
from django.contrib.auth.models import User
# Create your tests here.

comment = {
    'user_id': User.objects.get(pk=1),
    'lecture_id': 1,
    'slide_id': 1,
    'text': 'COMMENTARIY MAZAFAKA',
}

user = {
    'name': 'Test',
    'email': 'test@test.com',
    'password': 'testtest123'
}

class CommentsTests(APITestCase):
    def setUp(self):
        User.objects.create(
            username=user['name'], email=user['email'], password=user['password']
        )
       # Comment.objects.create(
       #     user_id=comment['user_id'], lecture_id=comment['lecture_id'], slide_id=comment['slide_id'], text=comment['text']
       # )

    def test_create_comment(self):
        res = self.client.post('course/comments/',
           {  
              'user_id': comment['user_id'],
              'lecture_id': comment['lecture_id'],
              'slide_id': comment['slide_id'],
              'text': comment['text']
             }
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

