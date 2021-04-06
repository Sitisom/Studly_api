from django.contrib import admin

# Register your models here.
from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass