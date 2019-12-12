from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from graphene_django.views import GraphQLView
from .schema import schema

# FIXME the codegen doesn't provide a csrf token
graphql = csrf_exempt(
  GraphQLView.as_view(graphiql=True, schema=schema)
)

urlpatterns = [
  path('admin/', admin.site.urls),
  path('graphql/', graphql),
  path('', TemplateView.as_view(template_name='index.html')),
]
