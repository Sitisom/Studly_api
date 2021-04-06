from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from tests.models import Assignment, AssignmentStatuses, TaskAnswer
from tests.serializers import AssignmentsSerializer


class TestsModelViewSet(ModelViewSet):
    pass


class TestAssignmentsViewSet(GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        return AssignmentsSerializer

    def get_queryset(self):
        qs = Assignment.objects.filter(student=self.request.user.student_profile)

        if self.action == 'list':
            qs = qs.filter(status=AssignmentStatuses.UNDONE.value)

        return qs


class TaskAnswerModelViewSet(GenericViewSet,
                             mixins.UpdateModelMixin):
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return TaskAnswer.objects.filter(student=self.request.user.student_profile)

    def get_object(self):
        return TaskAnswer.objects.get_or_create(student=self.request.user.student_profile,
                                                task_id=self.request.POST.get('task_id', None))

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        max_points = 100 / obj.task.test.tasks.count()

        obj.answer = self.request.POST.get('answer', None)
        obj.point = max_points if obj.answer == obj.task.right_answer else 0

        obj.save()
