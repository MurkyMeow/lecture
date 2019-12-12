from django.contrib.auth.models import User
from Education.test_case import LectureGraphQLTestCase

user = {
  'name': 'Test',
  'email': 'test@test.com',
  'password': 'testtest123'
}

signup_mutation = '''
  mutation signup($name: String!, $email: String!, $password: String!) {
    signup(name: $name, email: $email, password: $password) {
      user {
        username
        email
      }
      conflict {
        name
        email
      }
    }
  }
'''

class AuthTest(LectureGraphQLTestCase):
  def setUp(self):
    self.user = User.objects.create_user(
      username=user['name'], email=user['email'], password=user['password']
    )

  def test_create_account(self):
    variables = {
      'name': 'RulonOboev',
      'email': 'fuckyouhoney@gmail.com',
      'password': 'getoverhere',
    }
    res = self.query(signup_mutation, variables=variables)
    self.assertResponseNoErrors(res)
    resUser = res['data']['signup']['user']
    self.assertEqual(resUser['username'], variables['name'])
    self.assertEqual(resUser['email'], variables['email'])

  def test_login(self):
    variables = {
      'email': user['email'],
      'password': user['password'],
    }
    res = self.query('''
      mutation signin($email: String!, $password: String!) {
        signin(email: $email, password: $password) {
          user { email }
        }
      }
    ''', variables=variables)
    self.assertResponseNoErrors(res)
    resUser = res['data']['signin']['user']
    self.assertEqual(resUser['email'], variables['email'])

  def test_signup_name_conflict(self):
    res = self.query(signup_mutation, variables={
      'name': user['name'], 'email': 'z', 'password': 'z',
    })
    self.assertResponseNoErrors(res)
    conflict = res['data']['signup']['conflict']
    self.assertTrue(conflict['name'])

  def test_signup_email_conflict(self):
    res = self.query(signup_mutation, variables={
      'email': user['email'], 'name': 'z', 'password': 'z',
    })
    self.assertResponseNoErrors(res)
    conflict = res['data']['signup']['conflict']
    self.assertTrue(conflict['email'])

  def test_user_data(self):
    self.force_login(self.user)
    res = self.query('''
      query {
        me {
          username
          email
        }
      }
    ''')
    self.assertResponseNoErrors(res)
    resUser = res['data']['me']
    self.assertEqual(resUser['username'], self.user.username)
    self.assertEqual(resUser['email'], self.user.email)
