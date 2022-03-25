from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.models import Rating
from lessons.models import Assignment, Statuses, Answer
from lessons.serializers import AssignmentsSerializer


class AssignmentsViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin):
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        return AssignmentsSerializer

    def get_queryset(self):
        qs = Assignment.objects.filter(student=self.request.user.student_profile)

        if self.action == 'list':
            qs = qs.filter(status=Statuses.UNDONE.value)

        return qs


class TaskAnswerModelViewSet(GenericViewSet,
                             mixins.UpdateModelMixin):
    permission_classes = ()

    def get_queryset(self):
        return Answer.objects.filter(student=self.request.user.student_profile)

    def get_object(self):
        task, _ = Answer.objects.get_or_create(student=self.request.user.student_profile,
                                                   task_id=self.request.POST.get('taskId'))
        return task

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        max_points = 100 / obj.task.lesson.tasks.count()

        obj.answer = self.request.POST.get('answer', None)
        obj.points = max_points if obj.answer == obj.task.right_answer else 0
        obj.save()

        rating = Rating.objects.get(user=self.request.user)
        rating.rating += obj.points
        rating.save()

        return Response({'detail': 'success', 'points': obj.points}, status=200)
