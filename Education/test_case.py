import json
from graphene_django.utils.testing import GraphQLTestCase
from Education.schema import schema

# some hacks and sugar for the GraphQLTestCase
class LectureGraphQLTestCase(GraphQLTestCase):
  GRAPHQL_SCHEMA = schema

  # overriding because i dont want to call
  # `json.loads` every time i make a request!
  def query(self, query, op_name=None, input_data=None, variables=None):
    resp = super().query(query, op_name, input_data, variables)
    return json.loads(resp.content)

  # overriding to actually print the errors to the console!
  def assertResponseNoErrors(self, content):
    self.assertNotIn('errors', list(content.keys()), content)

  # dangerously accessing a private member
  # because the public one doesn't work!
  def force_login(self, user):
    self._client.force_login(user)
