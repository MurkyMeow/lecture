import os, json, sys, django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Education.settings')
django.setup()

from MainApp.models import Course, Lecture, Slide

def run(course_dir = 'courses/'):
    Course.objects.all().delete()

    for filename in os.listdir(course_dir):
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
