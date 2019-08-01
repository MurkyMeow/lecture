from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from .serializers import *

# Create your views here.


@api_view(['POST'])
def SignupView(request):
    new_user = User.objects.create(
        name = request.POST.get("name"),
        email = request.POST.get("email"),
        password = request.POST.get("password")
    )
    if User.objects.filter(email=email).exists():  
        return Response(status=HTTP_409_CONFLICT)
    try:
        validate_password(new_user.password)
        new_user.save()
        response = Response( {'ok': True})
        response.set_cookie('user_id', new_user.id)
        return response
    except ValidationError:
        return Response(status=HTTP_406_NOT_ACCEPTABLE)


@api_view(['POST'])
def SigninView(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    authorized_user = User.objects.get(email=email)
    if authorized_user.password == password:
        authorized_user.is_authenticated = True
        response = Response( {'ok': True}, status=HTTP_200_OK)
        response.set_cookie('user_id', authorized_user.id)
        return response
    else:
        return Response(status=HTTP_401_UNAUTHORIZED)
