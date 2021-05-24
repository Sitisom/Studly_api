from django.contrib import admin

# Register your models here.
from lessons.models import Lesson, Task, Variant, Assignment, LessonAttachments


@admin.register(Lesson)
class TestAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class TestAssignmentAdmin(admin.ModelAdmin):
    exclude = ('status', )


@admin.register(LessonAttachments)
class TestAttachmentsAdmin(admin.ModelAdmin):
    pass
