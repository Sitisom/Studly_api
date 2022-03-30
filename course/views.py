from datetime import datetime

from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from course.models import Course, Subscription, RatePlan
from course.serializers import CourseSerializer, RatePlanSerializer


class CourseViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = CourseSerializer

    @action(methods=['GET'], detail=False)
    def my(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(methods=['GET'], detail=False)
    def buy(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(methods=['POST'], detail=False)
    def subscribe(self, request, *args, **kwargs):
        course = Course.objects.get(id=self.request.POST.get('courseID'))
        Subscription.objects.create(
            user=self.request.user,
            course=course,
            date=datetime.now()
        )
        return Response('Created', status=status.HTTP_201_CREATED)

    @staticmethod
    def init_queryset():
        return Course.objects.filter(is_active=True)

    def my_queryset(self, qs):
        return qs.filter(subscriptions__user=self.request.user)

    def buy_queryset(self, qs):
        return qs.exclude(subscriptions__user=self.request.user)

    def get_queryset(self):
        qs = self.init_queryset()
        if self.action == 'my':
            qs = self.my_queryset(qs)
        if self.action == 'buy':
            qs = self.buy_queryset(qs)
        return qs


class RatePlanViewSet(viewsets.ModelViewSet):
    serializer_class = RatePlanSerializer

    def get_queryset(self):
        return RatePlan.objects.filter(is_active=True)
