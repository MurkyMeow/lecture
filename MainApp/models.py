from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Course(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class Lecture(models.Model):

    course = models.ForeignKey("Course", null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=300)
    background = models.CharField(max_length=50)

    def __str__(self):
        return self.id


class Slide(models.Model):

    course = models.ForeignKey("Course", null=True, on_delete=models.CASCADE)
    lecture = models.ForeignKey("Lecture", null=True, on_delete=models.CASCADE)
    title =  models.CharField(max_length=150)
    content = models.TextField()

    def __str__(self):
        return self.id


class Exercise(models.Model):

    for_lecture = models.ForeignKey("Lecture", null=True, on_delete=models.CASCADE)
    task = models.TextField()

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.id


class Answer(models.Model):

    for_exercise = models.ForeignKey("Exercise", null=True, on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    correct = models.BooleanField()

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.id


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    course = models.ForeignKey("Course", null=True, on_delete=models.CASCADE)
    lecture = models.ForeignKey("Lecture", null=True, on_delete=models.CASCADE)
    slide = models.ForeignKey("Slide", null=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    published = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.id


class Progress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey("Course", null=True, on_delete=models.CASCADE)
    lecture = models.ForeignKey("Lecture", null=True, on_delete=models.CASCADE)
    slide = models.ForeignKey("Slide", null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Progress"
        verbose_name_plural = "Progress"

    def __str__(self):
        return self.id