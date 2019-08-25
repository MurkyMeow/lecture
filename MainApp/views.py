from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


def LectureView(request, course, lecture):
    return render(request, 'lecture-temlpate.html', context={
      'course': course,
      'lecture': lecture,
    })

def EmptyStringValidator(string):
    if string == '' or string == None:
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class APIComments(APIView):
    def post(self, request):
        #if request.data.get('text') == '' or request.data.get('text') == None:
        #    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        return EmptyStringValidator(request.data.get('text'))
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
        try:
            comment = Comment.objects.get(pk=request.data.get('comment_id'))
        except Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return EmptyStringValidator(request.data.get('text'))
        #if request.data.get('text') == '' or request.data.get('text') == None:
        #    return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
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
            lecture_id=request.data.get('lecture_id'),
            slide_id=request.data.get('slide_id'),
        )
        serializer = ProgressSerializer(new_progress)
        return Response(serializer.data)

    def get(self, request):
        progress = Progress.objects.filter(
            user=request.user
        )
        serializer = ProgressSerializer(progress, many=True)
        return Response(serializer.data)