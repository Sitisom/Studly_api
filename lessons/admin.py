from django.contrib import admin

# Register your models here.
from lessons.models import Lesson, Task, Variant, Assignment, LessonAttachments, Topic


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    exclude = ('status', )


@admin.register(LessonAttachments)
class LessonAttachmentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
