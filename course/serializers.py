from django.db.models import Count
from rest_framework import serializers

from core.serializers import UserSerializer
from course.models import Course, Subject, Subscription, RatePlan
from lessons.models import Statuses
from lessons.serializers import LessonSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class RatePlanSerializer(serializers.ModelSerializer):
    current = serializers.SerializerMethodField()

    def get_current(self, obj):
        if hasattr(obj, 'current'):
            return obj.current
        return False

    class Meta:
        model = RatePlan
        fields = ["id", "title", "price", "order", "current", ]


class CourseSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.title')
    teacher = UserSerializer()
    rate_plan = RatePlanSerializer()
    lessons = LessonSerializer(many=True)
    lessons_count = serializers.SerializerMethodField()
    tasks_count = serializers.SerializerMethodField()
    completed_lessons = serializers.SerializerMethodField()
    subscribed = serializers.SerializerMethodField()

    def get_subscribed(self, obj):
        if request := self.context.get('request'):
            return obj.id in request.user.student_courses.values_list('course_id', flat=True)
        return False

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_completed_lessons(self, obj):
        return obj.lessons.filter(assignments__status=Statuses.DONE.value).count()

    def get_tasks_count(self, obj):
        return obj.lessons.aggregate(Count('tasks'))['tasks__count']

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    rate_plan = RatePlanSerializer()

    class Meta:
        model = Subscription
        fields = '__all__'


class PurchaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)
    price = serializers.IntegerField(min_value=0)
