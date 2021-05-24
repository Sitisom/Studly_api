from django.contrib import admin

# Register your models here.
from course.models import Course, Difficulty, Subject, CourseSubscription


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'difficulty', 'teacher',)

    class Meta:
        fields = '__all__'


@admin.register(Difficulty)
class DifficultyAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


@admin.register(CourseSubscription)
class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('course', )

    class Meta:
        fields = '__all__'
