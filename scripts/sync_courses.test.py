import os
from sync_courses import run

MOCK_DIR = 'scripts/courses_mock'

run(course_dir=MOCK_DIR)

from MainApp.models import Course, Lecture, Slide

def main():
  print('First run')

  names = list(
    map(lambda x: x.strip('.json'), os.listdir(MOCK_DIR)),
  )

  objects = Course.objects.all()

  assert len(objects) == len(names), 'The amount of objects does not match the amount of files'

  for obj in objects:
    assert obj.name in names, f'The script produced a course with unknown name "{obj.name}"'

  print('OK')
  print('Second run')

  run(course_dir=MOCK_DIR)

  next_objects = Course.objects.all()

  assert len(objects) == len(next_objects), 'The second run produced more or less objects than the previous one'

  for (obj, n_obj) in zip(objects, next_objects):
    assert obj.name == n_obj.name, f'Name mismatch: {obj.name} != {n_obj.name}'
    assert obj.id == n_obj.id, f'Id mismatch: {obj.id} != {n_obj.id}'

  print('OK')

main()
