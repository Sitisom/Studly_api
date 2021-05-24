from rest_framework import routers

from course.views import CourseViewSet

router = routers.DefaultRouter()
router.register('', CourseViewSet, 'courses')

urlpatterns = [

] + router.urls
