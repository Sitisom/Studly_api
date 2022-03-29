from rest_framework import serializers

from core.serializers import UserSerializer
from course.models import Course, Difficulty, Subject, Subscription
from lessons.models import Statuses
from lessons.serializers import LessonSerializer


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    difficulty = serializers.CharField(source='difficulty.title')
    subject = serializers.CharField(source='subject.title')
    teacher = UserSerializer()
    lessons = LessonSerializer(many=True)
    lessons_count = serializers.SerializerMethodField()
    completed_lessons = serializers.SerializerMethodField()

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    def get_completed_lessons(self, obj):
        return obj.lessons.filter(lesson_assignment__status=Statuses.DONE.value).count()

    class Meta:
        model = Course
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
