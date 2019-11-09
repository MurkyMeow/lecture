import graphene
from django.core.exceptions import ValidationError
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.password_validation import validate_password
from graphene_django import DjangoObjectType
from MainApp.models import User

class UserType(DjangoObjectType):
  class Meta:
    model = User
    fields = ('id', 'username', 'email')

class SigninUser(graphene.Mutation):
  class Arguments:
    email = graphene.String(required=True)
    password = graphene.String(required=True)

  user = graphene.Field(UserType)

  def mutate(self, info, email, password):
    try:
      user = User.objects.get(email=email)
    except User.DoesNotExist:
      return None
    if check_password(password, user.password):
      login(info.context, user)
      return SigninUser(user=user)
    return None

class SignupConflict(graphene.ObjectType):
  name = graphene.Boolean()
  email = graphene.Boolean()

class SignupUser(graphene.Mutation):
  class Arguments:
    name = graphene.String(required=True)
    email = graphene.String(required=True)
    password = graphene.String(required=True)

  user = graphene.Field(UserType)
  conflict = graphene.Field(SignupConflict)

  def mutate(self, info, name, email, password):
    conflict = SignupConflict(
      name=User.objects.filter(username=name).exists(),
      email=User.objects.filter(email=email).exists(),
    )
    if conflict.email or conflict.name:
      return SignupUser(conflict=conflict)
    try:
      validate_password(password)
    except ValidationError:
      return None
    user = User.objects.create_user(email=email, password=password, username=name)
    login(info.context, user)
    return SignupUser(user=user)

class SignoutUser(graphene.Mutation):
  ok = graphene.Boolean()

  def mutate(self, info):
    logout(info.context)
    return SignoutUser(ok=True)

class Mutation(graphene.ObjectType):
  signin = SigninUser.Field()
  signup = SignupUser.Field()
  signout = SignoutUser.Field()

class Query(graphene.ObjectType):
  me = graphene.Field(UserType)

  def resolve_me(self, info):
    return info.context.user
