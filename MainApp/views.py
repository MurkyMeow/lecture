from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
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
            lecture_id=request.data.get('lecture_id'),
            slide_id=request.data.get('slide_id'),
            text=request.data.get('text'),
        )
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data)

    def get(self, request):
        comments = Comment.objects.filter(
            lecture_id=request.GET.get('lecture_id'),
            slide_id=request.GET.get('slide_id'),
        )
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def patch(self, request):
        validate_comment(request.data)
        try:
            comment = Comment.objects.get(pk=request.data.get('comment_id'))
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        comment.text = request.data.get('text')
        comment.save()
        serializer = CommentSerializer(comment)
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
            lecture_id=request.GET.get('lecture_id'),
            slide_id=request.GET.get('slide_id'),
        )
        serializer = ProgressSerializer(new_progress)
        return Response(serializer.data)

    def get(self, request):
        progress = Progress.objects.filter(
            user=request.user
        )
        serializer = ProgressSerializer(progress, many=True)
        return Response(serializer.data)