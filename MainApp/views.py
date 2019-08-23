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

class APIComments(APIView):
    def post(self, request):
        new_comment = Comment.objects.create(
            user_id=request.user,
            lecture_id=request.data.get('lectureID'),
            slide_id=request.data.get('slideID'),
            text=request.data.get('text'),
        )
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data)

    def get(self, request):
        comments = Comment.objects.filter(
            lecture_id=request.data.get('lectureID'),
            slide_id=request.data.get('slideID'),
        )
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def patch(self, request):
        comment = Comment.objects.get(pk=request.data.get('commentID'))
        comment.text = request.data.get('text')
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request):
        comment = Comment.objects.get(pk=request.data.get('commentID'))
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)