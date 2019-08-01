from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .serializers import *

# Create your views here.

def credentials(user):
    response = Response(status=HTTP_200_OK)
    response.set_cookie('user_id', user.id)
    return response

@api_view(['POST'])
def SignupView(request):
    email = request.POST.get('email')
    if User.objects.filter(email=email).exists():
        return Response(status=HTTP_409_CONFLICT)
    try:
        new_user = User.objects.create(
            email = email,
            first_name = request.POST.get('name'),
            password = request.POST.get('password')
        )
        validate_password(new_user.password)
        new_user.save()
        return credentials(new_user)
    except ValidationError:
        return Response(status=HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def SigninView(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    user = User.objects.get(email=email)
    if user.password == password:
        return credentials(user)
    return Response(status=HTTP_403_FORBIDDEN)
