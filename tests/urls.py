from rest_framework import routers

from tests.views import TestAssignmentsViewSet

router = routers.DefaultRouter()

router.register('assignments', TestAssignmentsViewSet, 'assignments')

urlpatterns = [

]

urlpatterns += router.urls
