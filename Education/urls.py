from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

docs_view = get_schema_view(
    openapi.Info(title="Api docs", default_version='v1'),
)

urlpatterns = [
    path('api-docs', docs_view.with_ui('swagger')),
    path('course/', include('MainApp.urls')),
    path('auth/', include('AuthApp.urls')),
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html')),
]
