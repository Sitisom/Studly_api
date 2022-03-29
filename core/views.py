from django.db.models import FilteredRelation, Q
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet, ReadOnlyModelViewSet

# Create your views here.
from core.models import Rating, User
from core.serializers import RatingSerializer, ProfileSerializer


class RatingModelViewSet(ModelViewSet):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.order_by('rating')


class ProfileViewSet(ReadOnlyModelViewSet):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return User.objects.prefetch_related('subscriptions')

    @action(["GET"], detail=False)
    def my(self, request):
        return Response(self.serializer_class(request.user).data, 200)
