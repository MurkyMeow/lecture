from Education.test_case import LectureGraphQLTestCase
from .models import Comment, Course, Lecture, Slide
from django.contrib.auth.models import User

user = {
    'name': 'Test',
    'email': 'test@test.com',
    'password': 'testtest123'
}

# class GetControllersTest(APITestCase):
#     def setUp(self):
#         course = Course.objects.create(name='course_1')
#         lecture = Lecture.objects.create(
#             course=course, title='lec_1', subtitle='lec_1_subtitle', background='#fff'
#         )
#         slide = Slide.objects.create(
#             lecture=lecture, title='slide_1_title', content='slide_1_content'
#         )

#         def test_get_all_courses(self):
#             res = self.client.get('/course/courses/')
#             self.assertEqual(res.status_code, status.HTTP_200_OK)

#         def test_get_lectures(self):
#             params = { 'course_id': course.id }
#             res = self.client.get('/course/lectures/', params)
#             self.assertEqual(res.status_code, status.HTTP_200_OK)

#         def test_get_slides(self):
#             params = { 'lecture_id': lecture.id }
#             res = self.client.get('/course/slides/', params)
#             self.assertEqual(res.status_code, status.HTTP_200_OK)

class CommentsTests(LectureGraphQLTestCase):
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
    self.force_login(u)

  def test_get_comments(self):
    variables = { 'lectureId': 1, 'slideId': 1 }
    res = self.query('''
      query getComments($lectureId: Int!, $slideId: Int!) {
        comments(lectureId: $lectureId, slideId: $slideId) {
          text
        }
      }
    ''', variables=variables)
    self.assertResponseNoErrors(res)
    resComments = res['data']['comments']
    self.assertEqual(len(resComments), len(self.comments))

  def test_create_comment(self):
    variables = { 'lectureId': 1, 'slideId': 1, 'text': 'qwerqwer' }
    res = self.query('''
      mutation createComment($text: String!, $slideId: Int!, $lectureId: Int!) {
        createComment(text: $text, slideId: $slideId, lectureId: $lectureId) {
          comment {
            text
          }
        }
      }
    ''', variables=variables)
    self.assertResponseNoErrors(res)
    resComment = res['data']['createComment']['comment']
    self.assertEqual(resComment['text'], variables['text'])

  # def test_patch_comment(self):
  #   comment = { 'text': 'qwerqwer', 'comment_id': 1 }
  #   res = self.client.patch('/course/comments/', comment)
  #   self.assertEqual(res.status_code, status.HTTP_200_OK)
  #   self.assertEqual(res.data['text'], comment['text'])

  # def test_delete_comment(self):
  #   comment = { 'comment_id': 1 }
  #   res = self.client.delete('/course/comments/', comment)
  #   self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

  # def test_create_comment_validation(self):
  #   comment = { 'lecture_id': 1, 'slide_id': 1, 'text': '' }
  #   res = self.client.post('/course/comments/', comment)
  #   self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

  # def test_delete_comment_validation(self):
  #   comment = { 'comment_id': 101 }
  #   res = self.client.delete('/course/comments/', comment)
  #   self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
