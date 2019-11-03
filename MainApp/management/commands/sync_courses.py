import os, json
from django.core.management.base import BaseCommand, CommandError
from MainApp.models import Course, Lecture, Slide

class Command(BaseCommand):
  help = 'Adds the courses to the database'
  def add_arguments(self, parser):
    parser.add_argument('course_dir', type=str)
  def handle(self, *args, **options):
    course_dir = options['course_dir']
    all_courses = Course.objects.all()
    for course_file in os.listdir(course_dir):
      file = open(f'{course_dir}/{course_file}', encoding='utf-8')
      data = json.load(file)
      file.close()
      course_name = course_file.strip('.json')
      try:
        course_inst = Course.objects.get(name=course_name)
      except:
        course_inst = Course.objects.create(name=course_name)
      for lecture in data:
        try:
          lecture_inst = Lecture.objects.get(pk=lecture['id'])
          lecture_inst.course = course_inst
          lecture_inst.title = lecture['title']
          lecture_inst.subtitle = lecture['subtitle']
          lecture_inst.background = lecture['background']
          lecture_inst.save()
        except:
          lecture_inst = Lecture.objects.create(
            course=course_inst,
            title=lecture['title'],
            subtitle=lecture['subtitle'],
            background=lecture['background'],
          )
        for slide in lecture['slides']:
          try:
            slide_inst = Slide.objects.get(pk=slide['id'])
            slide_inst.lecture = lecture_inst
            slide_inst.title = slide['title']
            slide_inst.content = slide['content']
            slide_inst.save()
          except:
            slide_inst = Slide.objects.create(
              lecture=lecture_inst,
              title=slide['title'],
              content=slide['content'],
            )
    for course in all_courses:
      if not course.name + '.json' in os.listdir(course_dir):
        course.delete()
    self.stdout.write(self.style.SUCCESS(f'Synced {len(os.listdir(course_dir))} courses'))
