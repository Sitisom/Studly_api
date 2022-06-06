from django.contrib import admin

# Register your models here.
from lessons.models import Lesson, Task, Variant, Assignment, LessonAttachments, Topic, TaskVariantThroughModel


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    pass


class VariantInline(admin.TabularInline):
    model = TaskVariantThroughModel


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [VariantInline, ]


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    exclude = ('status', )


@admin.register(LessonAttachments)
class LessonAttachmentsAdmin(admin.ModelAdmin):
    pass


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    pass
