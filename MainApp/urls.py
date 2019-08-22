from django.urls import path, include
from .views import *

urlpatterns = [
    path('<str:course>/<int:lecture>/', LectureView),
    path('comments/', APIComments),
]
