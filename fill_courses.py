import os
import json
import sys

if __name__ == '__main__':
    sys.path.append(os.getcwd())
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Education.settings")
    import django
    django.setup()

from MainApp.models import Course, Lecture, Slide
listOfFile = os.listdir(path="courses/")

for course in Course.objects.all():
    course.delete()
for filename in listOfFile:
  new_course = Course.objects.create(name=filename.strip(".json"))
  with open('{filename}'.format(filename=filename), 'r', encoding='utf-8') as fh:
      data = json.load(fh)
  for lecture in data:
      new_lecture = Lecture.objects.create(
          course=new_course,
          title=lecture['title'],
          subtitle=lecture['subtitle'],
          background=lecture['background'] )
      for slide in lecture['slides']:
          new_slide = Slide.objects.create(lecture=new_lecture, title=slide['title'], content=slide['content'])