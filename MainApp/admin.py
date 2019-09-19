from django.contrib import admin
from .models import *

# Register your models here.

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("for_lecture", )
    list_display_links = ("for_lecture", )
    search_fields = ("for_lecture", "task")

class AnswerAdmin(admin.ModelAdmin):
    list_display = ("for_exercise", )
    list_display_links = ("for_exercise", )
    search_fields = ("for_exercise", "option", "correct")

admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Answer, AnswerAdmin)