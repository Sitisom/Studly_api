from rest_framework import serializers

from core.serializers import UserSerializer
from lessons.models import Assignment, Lesson, Task, Variant, LessonAttachments


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    given_answer = serializers.SerializerMethodField()
    points = serializers.SerializerMethodField()

    def answer_obj(self, obj):
        return obj.answers.get_or_create(student=self.context['request'].user.student_profile)[0]

    def get_given_answer(self, obj):
        return self.answer_obj(obj).answer

    def get_points(self, obj):
        return self.answer_obj(obj).points

    class Meta:
        model = Task
        fields = ('id', 'question', 'variants', 'given_answer', 'points')


class LessonAttachmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonAttachments
        fields = ('text', 'file', 'video_url')


class LessonSerializer(serializers.ModelSerializer):
    """
    Some comment
    """
    tasks = TaskSerializer(many=True)
    image = serializers.SerializerMethodField()
    topic = serializers.CharField(source='topic.title')
    course = serializers.CharField(source='course.title')

    def get_image(self, obj):
        return obj.image.url if obj.image else obj.course.image.url if obj.course else None

    class Meta:
        model = Lesson
        fields = '__all__'


class AssignmentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='lesson.title')
    count = serializers.IntegerField(source='lesson.tasks.count')

    teacher = UserSerializer(source='teacher.user')

    lesson = LessonSerializer()
    attachments = LessonAttachmentsSerializer(source='lesson.attachments')

    def get_teacher(self, obj):
        return '%s %s' % (obj.teacher.user.first_name, obj.teacher.user.last_name)

    class Meta:
        model = Assignment
        fields = '__all__'
