from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from AuthApp.serializers import UserSerializer
from .models import *
from .serializers import *

def LectureView(request, course, lecture):
    return render(request, 'lecture-temlpate.html', context={
      'course': course,
      'lecture': lecture,
    })

def validate_comment(data):
    if not data.get('text'): raise ValidationError('`text` cant be empty')

@api_view(['GET'])
def GetAllCourses(request):
    serializer = CourseSerializer(Course.objects.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetLectures(request):
    serializer = LectureSerializer(Lecture.objects.filter(course=request.GET.get('course_id')), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GetSlides(request):
    serializer = SlideSerializer(Slide.objects.filter(lecture=request.GET.get('lecture_id')), many=True)
    return Response(serializer.data)

class APIComments(APIView):
    def post(self, request):
        validate_comment(request.data)
        new_comment = Comment.objects.create(
            user=request.user,
            course=Course.objects.get(pk=request.GET.get('course_id')),
            lecture=Lecture.objects.get(pk=request.data.get('lecture_id')),
            slide=Slide.objects.get(pk=request.data.get('slide_id')),
            text=request.data.get('text'),
        )
        serializer = CommentSerializer(new_comment)
        serializer.data[0]['user'] = UserSerializer(User.objects.get(pk=serializer.data[0]['user'])).data
        return Response(serializer.data)

    def get(self, request):
        comments = Comment.objects.filter(
            course=Course.objects.get(pk=request.GET.get('course_id')),
            lecture=Lecture.objects.get(pk=request.GET.get('lecture_id')),
            slide=Slide.objects.get(pk=request.GET.get('slide_id')),
        )
        for comment in comments:
            comment['user'] = UserSerializer(User.objects.get(pk=comment.user))
        serializer = CommentSerializer(comments, many=True)
        for comment in serializer.data:
            comment['user'] = UserSerializer(User.objects.get(pk=comment['user'])).data
        return Response(serializer.data)

    def patch(self, request):
        validate_comment(request.data)
        try:
            comment = Comment.objects.get(pk=request.data.get('comment'))
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        comment.text = request.data.get('text')
        comment.save()
        serializer = CommentSerializer(comment)
        serializer.data[0]['user'] = UserSerializer(User.objects.get(pk=serializer.data[0]['user'])).data
        return Response(serializer.data)

    def delete(self, request):
        try:
            comment = Comment.objects.get(pk=request.data.get('comment_id'))
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class APIProgress(APIView):
    def post(self, request):
        new_progress = Progress.objects.create(
            user=request.user,
            course=Course.objects.get(pk=request.GET.get('course_id')),
            lecture=Lecture.objects.get(pk=request.GET.get('lecture_id')),
            slide=Slide.objects.get(pk=request.GET.get('slide_id')),
        )
        serializer = ProgressSerializer(new_progress)
        return Response(serializer.data)

    def get(self, request):
        progress = Progress.objects.filter(
            user=request.user
        )
        serializer = ProgressSerializer(progress, many=True)
        return Response(serializer.data)