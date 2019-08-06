from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def credentials(req, user):
    login(req, user)
    return Response(status=status.HTTP_200_OK)

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
    user = User.objects.create(email=email, password=password, username=name)
    return credentials(request, user)

@api_view(['POST'])
def SigninView(request):
    user = User.objects.get(email=request.data.get('email'))
    if user.password == request.data.get('password'):
        return credentials(request, user)
    return Response(status=status.HTTP_403_FORBIDDEN)

@api_view(['POST'])
def LogoutView(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)