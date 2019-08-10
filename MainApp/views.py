from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status
import os.path
# Create your views here.

def CoursesView(request):
    filepath = 'courses/preview.json'
    return FileResponse(open(filepath, 'rb'))


def LectureView(request, course, lecture):
    filepath = 'courses/{course}/{lecture}.html'.format(course=course, lecture=lecture)
    if os.path.isfile(filepath):
        return FileResponse(open(filepath, 'rb'))
    return Response(status=status.HTTP_404_NOT_FOUND)