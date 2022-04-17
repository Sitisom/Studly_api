from rest_framework import routers

from course.views import CourseViewSet, RatePlanViewSet

router = routers.DefaultRouter()
router.register("", CourseViewSet, "courses")
router.register("rate-plan", RatePlanViewSet, "rate-plan")

urlpatterns = [] + router.urls
