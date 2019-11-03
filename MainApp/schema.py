import graphene
from graphene_django import DjangoObjectType
from .models import Comment, Course, Progress

class CourseType(DjangoObjectType):
  class Meta:
    model = Course

class CommentType(DjangoObjectType):
  class Meta:
    model = Comment

class CreateComment(graphene.Mutation):
  class Arguments:
    text = graphene.String(required=True)
    slide_id = graphene.Int(required=True)
    lecture_id = graphene.Int(required=True)

  comment = graphene.Field(CommentType)

  def mutate(self, info, text, slide_id, lecture_id):
    return CreateComment(comment=Comment.objects.create(
      user=info.context.user,
      text=text,
      slide_id=slide_id,
      lecture_id=lecture_id,
    ))

class ProgressType(DjangoObjectType):
  class Meta:
    model = Progress

class Query(graphene.ObjectType):
  comments = graphene.List(
    CommentType,
    lecture_id=graphene.Int(required=True),
    slide_id=graphene.Int(required=True),
  )
  courses = graphene.List(CourseType)
  progress = graphene.List(ProgressType)

  def resolve_comments(self, info, lecture_id, slide_id):
    return Comment.objects.filter(lecture_id=lecture_id, slide_id=slide_id)

  def resolve_courses(self, info):
    return Course.objects.all()

  def resolve_progress(self, info):
    return Progress.objects.filter(user=info.context.user)

class Mutation(graphene.ObjectType):
  create_comment = CreateComment.Field()
