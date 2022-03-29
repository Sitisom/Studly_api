from rest_framework import routers

from core.views import RatingModelViewSet, ProfileViewSet

router = routers.DefaultRouter()
router.register('ratings', RatingModelViewSet, 'ratings')
router.register('profile', ProfileViewSet, 'profile')
urlpatterns = [] + router.urls
