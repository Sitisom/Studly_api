from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from core.models import Rating
from lessons.models import Assignment, Statuses, Answer, Lesson, TaskVariantThroughModel
from lessons.serializers import AssignmentsSerializer, LessonSerializer


class LessonViewSet(GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin):
    permission_classes = (IsAuthenticated, )
    serializer_class = LessonSerializer
    lookup_value_regex = "\d+"

    def get_queryset(self):
        return Lesson.objects.filter(course__in=self.request.user.student_courses.values('course_id'))

    @action(['POST'], detail=True)
    def watched(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.status != Statuses.DONE.value:
            obj.status = Statuses.DONE.value
            obj.save()


class AssignmentsViewSet(GenericViewSet,
                         mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin):
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        return AssignmentsSerializer

    def get_queryset(self):
        qs = Lesson.objects.filter(tasks__isnull=False)

        if self.action == 'list':
            qs = qs.filter(status=Statuses.UNDONE.value)

        return qs


class TaskAnswerModelViewSet(GenericViewSet,
                             mixins.UpdateModelMixin):
    permission_classes = ()

    def get_queryset(self):
        return Answer.objects.filter(student=self.request.user.student_profile)

    def get_object(self):
        task, _ = Answer.objects.get_or_create(
            user=self.request.user,
            task_id=self.request.data.get('task_id')
        )
        return task

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        max_points = 100 / obj.task.lesson.tasks.count()

        obj.answers.add(self.request.data.get('answer', None))
        obj.points = (
            max_points
            if (obj.answers.values_list('id', flat=True)
                in TaskVariantThroughModel.objects.filter(
                        task=obj.task,
                        is_right=True
                    ).values_list('variant_id', flat=True))
            else 0
        )
        obj.save()

        # rating = Rating.objects.get(user=self.request.user)
        # rating.rating += obj.points
        # rating.save()

        return Response({
            'task': obj.task.id,
            'points': obj.points,
            'given_answer': self.request.data.get('answer', None)
        }, status=200)
