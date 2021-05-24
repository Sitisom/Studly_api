from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet

# Create your views here.
from core.models import Rating
from core.serializers import RatingSerializer


class RatingModelViewSet(ModelViewSet):
    serializer_class = RatingSerializer

    def get_queryset(self):
        return Rating.objects.order_by('rating')
