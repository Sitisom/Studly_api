from django.contrib import admin
from django.urls import path
from rest_framework import routers

from core.views import RatingModelViewSet

router = routers.DefaultRouter()
router.register('ratings', RatingModelViewSet, 'ratings')
urlpatterns = [] + router.urls
