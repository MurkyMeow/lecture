import graphene
from graphene_django import DjangoObjectType
from .models import *

def validate_comment(data):
    if not data.get('text'): raise ValidationError('`text` cant be empty')

class CourseType(DjangoObjectType):
  class Meta:
    model = Course

class CommentType(DjangoObjectType):
  class Meta:
    model = Comment

class ProgressType(DjangoObjectType):
  class Meta:
    model = Progress

class LectureType(DjangoObjectType):
  class Meta:
    model = Lecture

class SlideType(DjangoObjectType):
  class Meta:
    model = Slide

class CreateComment(graphene.Mutation):
  class Arguments:
    text = graphene.String(required=True)
    slide_id = graphene.Int(required=True)
    lecture_id = graphene.Int(required=True)

  comment = graphene.Field(CommentType)

  def mutate(self, info, text, slide_id, lecture_id):
    validate_comment(request.data)
    return CreateComment(comment=Comment.objects.create(
      user=info.context.user,
      text=text,
      slide=slide_id,
      lecture=lecture_id,
    ))

class CreateProgress(graphene.Mutation):
  class Arguments:
    slide_id = graphene.Int(required=True)
    lecture_id = graphene.Int(required=True)

  progress = graphene.Field(CommentType)

  def mutate(self, info, text, slide_id, lecture_id):
    return CreateProgress(progress=Progress.objects.create(
      user=info.context.user,
      slide=slide_id,
      lecture=lecture_id,
    ))

class Query(graphene.ObjectType):
  comments = graphene.List(
    CommentType,
    lecture_id=graphene.Int(required=True),
    slide_id=graphene.Int(required=True),
  )
  courses = graphene.List(CourseType)
  progress = graphene.List(ProgressType)
  lectures = graphene.List(LectureType, 
    course_id=graphene.Int(required=True)
  )
  slides = graphene.List(SlideType, 
    course_id=graphene.Int(required=True)
  )

  def resolve_comments(self, info, lecture_id, slide_id):
    return Comment.objects.filter(lecture=lecture_id, slide=slide_id)

  def resolve_courses(self, info):
    return Course.objects.all()

  def resolve_progress(self, info):
    return Progress.objects.filter(user=info.context.user)

  def resolve_lectures(self, info, course_id):
    return Lecture.objects.filter(course=course_id)

  def resolve_slides(self, info, course_id):
    return Slide.objects.filter(course=course_id)

class Mutation(graphene.ObjectType):
  create_comment = CreateComment.Field()
  create_progress = CreateProgress.Field()
