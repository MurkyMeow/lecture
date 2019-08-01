from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *

# Create your views here.

def credentials(user):
    response = Response(status=status.HTTP_200_OK)
    response.set_cookie('user_id', user.id)
    return response

@api_view(['POST'])
def SignupView(request):
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')
    if User.objects.filter(Q(email=email) | Q(username=name)).exists():
        return Response(status=status.HTTP_409_CONFLICT)
    try:
        validate_password(password)
    except ValidationError:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    new_user = User.objects.create(email=email, password=password, username=name)
    return credentials(new_user)

@api_view(['POST'])
def SigninView(request):
    user = authenticate(
        username=request.data.get('name'),
        password=request.data.get('password'),
    )
    if user:
        return credentials(user)
    return Response(status=status.HTTP_403_FORBIDDEN)
