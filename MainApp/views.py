from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

def LectureView(request, course, lecture):
    return render(request, 'lecture-temlpate.html', context={
      'course': course,
      'lecture': lecture,
    } )

class APIComments(APIView):
    def post(self, request):
        user_id = request.user.id
        lecture_id = request.data.get('lectureID')
        slide_id = request.data.get('slideID')
        text = request.data.get('text')
        new_comment = Comment.objects.create(user_id=user_id, lecture_id=lecture_id, slide_id=slide_id, text=text)
        serializer = CommentSerializer(new_comment)
        return Response(serializer.data)

    def get(self, request):
        comments = Comment.objects.filter(lecture_id=lecture_id, slide_id=slide_id)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def patch(self, request):
        comment = Comment.objects.get(pk=request.data.get('commentID'))
        new_text = request.data.get('text')
        comment.text = new_text
        comment.save()
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request):
        comment = Comment.objects.get(pk=request.data.get('commentID'))
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)