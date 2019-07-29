from django.db import models

# Create your models here.
class Article(models.Model):

    title = models.CharField(max_length=300)
    explanation = models.TextField()

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"

    def __str__(self):
        return self.title


class Exercise(models.Model):

    for_article = models.ForeignKey("Article", on_delete=models.CASCADE)
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