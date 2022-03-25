from django.contrib import admin

# Register your models here.
from teachers.models import TeacherProfile


@admin.register(TeacherProfile)
class TeacherAdmin(admin.ModelAdmin):
    pass
