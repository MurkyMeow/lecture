import graphene
import AuthApp.schema
import MainApp.schema

class Query(
  MainApp.schema.Query,
  AuthApp.schema.Query,
  graphene.ObjectType
):
  pass

class Mutation(
  MainApp.schema.Mutation,
  AuthApp.schema.Mutation,
  graphene.ObjectType
):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)
