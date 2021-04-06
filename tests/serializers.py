from rest_framework import serializers

from core.serializers import UserSerializer
from tests.models import Assignment, Test, Task, Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    variants = VariantSerializer(many=True)

    class Meta:
        model = Task
        fields = '__all__'


class TestSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Test
        fields = '__all__'


class AssignmentsSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='test.title')
    count = serializers.IntegerField(source='test.tasks.count')

    teacher = UserSerializer(source='teacher.user')

    test = TestSerializer()

    def get_teacher(self, obj):
        return '%s %s' % (obj.teacher.user.first_name, obj.teacher.user.last_name)

    class Meta:
        model = Assignment
        fields = '__all__'
