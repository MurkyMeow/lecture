from rest_framework.test import APITestCase
from rest_framework import status
from .models import Comment, Course, Lecture, Slide
from django.contrib.auth.models import User

user = {
    'name': 'Test',
    'email': 'test@test.com',
    'password': 'testtest123'
}

class GetControllersTest(APITestCase):
    def setUp(self):
        course = Course.objects.create(name='course_1')
        lecture = Lecture.objects.create(
            course=course, title='lec_1', subtitle='lec_1_subtitle', background='#fff'
        )
        slide = Slide.objects.create(
            lecture=lecture, title='slide_1_title', content='slide_1_content'
        )

        def test_get_all_courses(self):
            res = self.client.get('/course/courses/')
            self.assertEqual(res.status_code, status.HTTP_200_OK)

        def test_get_lectures(self):
            params = { 'course_id': course.id }
            res = self.client.get('/course/lectures/', params)
            self.assertEqual(res.status_code, status.HTTP_200_OK)

        def test_get_slides(self):
            params = { 'lecture_id': lecture.id }
            res = self.client.get('/course/slides/', params)
            self.assertEqual(res.status_code, status.HTTP_200_OK)

class CommentsTests(APITestCase):
    def setUp(self):
        u = User.objects.create_user(
            username=user['name'], email=user['email'], password=user['password']
        )
        course = Course.objects.create(name='course_1')
        lecture = Lecture.objects.create(
            course=course, title='lec_1', subtitle='lec_1_subtitle', background='#fff'
        )
        slide = Slide.objects.create(
            lecture=lecture, title='slide_1_title', content='slide_1_content'
        )
        self.comments = [
            Comment.objects.create(user=u, lecture=lecture, slide=slide, text='foo'),
            Comment.objects.create(user=u, lecture=lecture, slide=slide, text='bar'),
        ]
        self.client.force_authenticate(u)

    def test_get_comments(self):
        res = self.client.get('/course/comments/', {
            'lecture_id': 1, 'slide_id': 1,
        })
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), len(self.comments))

    def test_comment_has_author(self):
        res = self.client.get('/course/comments/', {
            'lecture_id': 1, 'slide_id': 1,
        })
        comment_author = res.data[0].get('user')
        self.assertIsInstance(comment_author, dict)
        self.assertIn('id', comment_author)
        self.assertIn('username', comment_author)

    def test_create_comment(self):
        comment = { 'lecture_id': 1, 'slide_id': 1, 'text': 'qwerqwer' }
        res = self.client.post('/course/comments/', comment)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['text'], comment['text'])
        self.assertEqual(res.data['slide'], str(comment['slide_id']))
        self.assertEqual(res.data['lecture'], str(comment['lecture_id']))

    def test_patch_comment(self):
        comment = { 'text': 'qwerqwer', 'comment_id': 1 }
        res = self.client.patch('/course/comments/', comment)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['text'], comment['text'])

    def test_delete_comment(self):
        comment = { 'comment_id': 1 }
        res = self.client.delete('/course/comments/', comment)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_comment_validation(self):
        comment = { 'lecture_id': 1, 'slide_id': 1, 'text': '' }
        res = self.client.post('/course/comments/', comment)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_comment_validation(self):
        comment = { 'comment_id': 101 }
        res = self.client.delete('/course/comments/', comment)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
