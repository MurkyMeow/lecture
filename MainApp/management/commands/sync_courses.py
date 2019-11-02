import os, json
from django.core.management.base import BaseCommand, CommandError
from MainApp.models import Course, Lecture, Slide

class Command(BaseCommand):
    help = 'Adds the courses to the database'

    def add_arguments(self, parser):
        parser.add_argument('course_dir', type=str)

    def handle(self, *args, **options):
        Course.objects.all().delete()
        course_dir = options['course_dir']
        files = os.listdir(course_dir)
        for filename in files:
            file = open(f'{course_dir}/{filename}', encoding='utf-8')
            data = json.load(file)
            new_course = Course.objects.create(name=filename.strip('.json'))
            for lecture in data:
                new_lecture = Lecture.objects.create(
                    course=new_course,
                    title=lecture['title'],
                    subtitle=lecture['subtitle'],
                    background=lecture['background'],
                )
                for slide in lecture['slides']:
                    Slide.objects.create(
                        lecture=new_lecture,
                        title=slide['title'],
                        content=slide['content'],
                    )
        self.stdout.write(self.style.SUCCESS(f'Synced {len(files)} courses'))
