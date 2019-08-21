from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Exercise(models.Model):

    for_article = models.IntegerField()
    task = models.TextField()

    class Meta:
        verbose_name = "Exercise"
        verbose_name_plural = "Exercises"

    def __str__(self):
        return self.name


class Answer(models.Model):

    for_exercise = models.ForeignKey("Exercise", on_delete=models.CASCADE)
    option = models.CharField(max_length=100)
    correct = models.BooleanField()

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.name


class Comment(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    lecture_id = models.IntegerField()
    slide_id = models.IntegerField()
    text = models.TextField()

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.user_id, text 


class Progress(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    lecture_id = models.IntegerField()
    slide_id = models.IntegerField()

    class Meta:
        verbose_name = "Progress"
        verbose_name_plural = "Progress"

    def __str__(self):
        return self.user_id
