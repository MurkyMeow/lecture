from django.contrib import admin
from .models import *

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name",)
    list_display_links = ("name",)
    search_fields = ("name",)

class LectureAdmin(admin.ModelAdmin):
    list_display = ("course", "title", "subtitle", "background")
    list_display_links = ("course", "title", "subtitle", "background")
    search_fields = ("course", "title", "subtitle", "background")

class SlideAdmin(admin.ModelAdmin):
    list_display = ("course", "lecture", "title", "content")
    list_display_links = ("course", "lecture", "title", "content")
    search_fields = ("course" ,"lecture", "title", "subtitle")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "text", "published")
    list_display_links = ("user", "text", "published")
    search_fields = ("user", "text", "published")

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("for_lecture", "task")
    list_display_links = ("for_lecture", "task")
    search_fields = ("for_lecture", "task")

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("for_exercise", "option", "correct")
    list_display_links = ("for_exercise", "option", "correct")
    search_fields = ("for_exercise", "option", "correct")

class ProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "lecture", "slide")
    list_display_links = ("user", "course", "lecture", "slide")
    search_fields = ("user", "course", "lecture", "slide")

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lecture, LectureAdmin)
admin.site.register(Slide, SlideAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Progress, ProgressAdmin)