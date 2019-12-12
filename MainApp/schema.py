import graphene
from graphene_django import DjangoObjectType
from .models import *

def validate_comment(text):
    if not text: raise ValidationError('`text` cant be empty')

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
    validate_comment(text)
    return CreateComment(comment=Comment.objects.create(
      user=info.context.user,
      text=text,
      slide=Slide.objects.get(pk=slide_id),
      lecture=Lecture.objects.get(pk=lecture_id),
    ))
  
class PatchComment(graphene.Mutation):
  class Arguments:
    text = graphene.String(required=True)
    comment_id = graphene.Int(required=True)

  comment = graphene.Field(CommentType)

  def mutate(self, info, text, comment_id):
    validate_comment(text)
    try:
      comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    comment.text = text
    comment.save()
    return comment

class DeleteComment(graphene.Mutation):
  class Arguments:
    text = graphene.String(required=True)
    comment_id = graphene.Int(required=True)

  comment = graphene.Field(CommentType)

  def mutate(self, info, comment_id):
    try:
      comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)
    comment.delete()
    return comment

class CreateProgress(graphene.Mutation):
  class Arguments:
    slide_id = graphene.Int(required=True)
    lecture_id = graphene.Int(required=True)

  progress = graphene.Field(CommentType)

  def mutate(self, info, text, slide_id, lecture_id):
    return CreateProgress(progress=Progress.objects.create(
      user=info.context.user,
      slide=Slide.objects.get(pk=slide_id),
      lecture=Lecture.objects.get(pk=lecture_id),
    ))

class Query(graphene.ObjectType):
  particular_comments = graphene.List(CommentType,
    required=True,
    lecture_id=graphene.Int(required=True),
    slide_id=graphene.Int(required=True),
  )
  all_courses = graphene.List(CourseType,
    required=True,
  )
  particular_progress = graphene.List(ProgressType,
    required=True,
  )
  particular_lectures = graphene.List(LectureType,
    required=True,
    course_id=graphene.Int(required=True),
  )
  particular_slides = graphene.List(SlideType,
    required=True,
    course_id=graphene.Int(required=True),
  )

  def resolve_particular_comments(self, info, lecture_id, slide_id):
    return Comment.objects.filter(lecture=lecture_id, slide=slide_id)

  def resolve_all_courses(self, info):
    return Course.objects.all()

  def resolve_particular_progress(self, info):
    return Progress.objects.filter(user=info.context.user)

  def resolve_particular_lectures(self, info, course_id):
    return Lecture.objects.filter(course=course_id)

  def resolve_particular_slides(self, info, course_id):
    return Slide.objects.filter(course=course_id)

class Mutation(graphene.ObjectType):
  create_comment = CreateComment.Field(required=True)
  patch_comment = PatchComment.Field(required=True)
  delete_comment = DeleteComment.Field(required=True)
  create_progress = CreateProgress.Field(required=True)
