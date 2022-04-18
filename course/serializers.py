from rest_framework import serializers

from core.serializers import UserSerializer
from course.models import Course, Subject, Subscription, RatePlan
from lessons.models import Statuses
from lessons.serializers import LessonSerializer


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source='subject.title')
    teacher = UserSerializer()
    lessons = LessonSerializer(many=True)
    lessons_count = serializers.SerializerMethodField()
    completed_lessons = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_completed_lessons(self, obj):
        return obj.lessons.filter(assignments__status=Statuses.DONE.value).count()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class RatePlanSerializer(serializers.ModelSerializer):
    current = serializers.BooleanField()

    class Meta:
        model = RatePlan
        fields = ["id", "title", "price", "order", "current", ]


class PurchaseSerializer(serializers.Serializer):
    id = serializers.IntegerField(min_value=0)
    price = serializers.IntegerField(min_value=0)
