from django.shortcuts import render

def LectureView(request, course, lecture):
    return render(request, 'lecture-temlpate.html', context={
      'course': course,
      'lecture': lecture,
    })