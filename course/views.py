from datetime import datetime

from django.db.models import F, ExpressionWrapper, Value
from django.db.models.lookups import GreaterThan, Exact
from django.forms import BooleanField

from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from course.models import Course, Subscription, RatePlan, CourseSubscription
from course.serializers import CourseSerializer, RatePlanSerializer, PurchaseSerializer


class CourseViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = CourseSerializer
    lookup_value_regex = "\d+"

    @action(methods=['GET'], detail=False)
    def my(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(methods=['GET'], detail=False)
    def buy(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @action(methods=['POST'], detail=False)
    def subscribe(self, request, *args, **kwargs):
        course = Course.objects.get(id=self.request.data.get('id'))
        CourseSubscription.objects.create(
            user=self.request.user,
            course=course,
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
    model = RatePlan

    def get_queryset(self):
        subscription = self.request.user.subscriptions.filter(is_active=True).first()
        qs = RatePlan.objects.filter(is_active=True).annotate(current=Exact(F("id"), Value(subscription.rate_plan_id)))
        return qs

    @action(methods=['POST'], detail=False, url_name='purchase', url_path='purchase')
    def purchase(self, *args, **kwargs):
        ser = PurchaseSerializer(data=self.request.data)
        ser.is_valid(True)
        try:
            obj = self.get_queryset().get(id=ser.validated_data['id'])

            if obj.price != ser.validated_data['price']:
                raise ValidationError('Неверная цена покупки')
            elif obj.current:
                raise ValidationError('Тарифный план уже куплен')
            else:
                # Здесь должен проходить процесс оплаты, но мы просто создадим новую связь
                user = self.request.user
                current_sub = user.subscriptions.filter(is_active=True).first()
                current_sub.is_active = False
                current_sub.save()

                Subscription.objects.create(
                    user=user,
                    rate_plan=obj,
                    is_valid=True,
                    is_active=True
                )

        except self.model.DoesNotExist as e:
            return Response(f"Что-то пошло не так: {e}")