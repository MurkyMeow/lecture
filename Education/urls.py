from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from graphene_django.views import GraphQLView
import graphene
import AuthApp.schema
import MainApp.schema

# This class will inherit from multiple Queries
# as we begin to add more apps to our project
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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
    path('', TemplateView.as_view(template_name='index.html')),
]
