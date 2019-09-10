from django.urls import path, include
from .views import *

urlpatterns = [
    path('signin/', SigninView),
    path('signup/', SignupView),
    path('userdata/', UserDataView),
    path('logout/', LogoutView),
]
