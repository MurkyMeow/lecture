from django.urls import path, include
from .views import *

urlpatterns = [
    path('<str:course>/<int:lecture>/', LectureView),
    path('comments/', APIComments.as_view()),
    path('progress/', APIProgress.as_view()),
]
