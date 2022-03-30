from django.contrib import admin

# Register your models here.
from course.models import Course, Difficulty, Subject, Subscription, RatePlan


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


@admin.register(Subscription)
class CourseSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('rate_plan', )

    class Meta:
        fields = '__all__'


@admin.register(RatePlan)
class RatePlanAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'
