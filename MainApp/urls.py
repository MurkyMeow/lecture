from django.urls import path, include
from .views import *

urlpatterns = [
    path('', CoursesView),
    path('<str:course>/<int:lecture>/', LectureView),
]
