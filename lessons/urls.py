from rest_framework import routers

from lessons.views import TestAssignmentsViewSet, TaskAnswerModelViewSet

router = routers.DefaultRouter()

router.register('assignments', TestAssignmentsViewSet, 'assignments')
router.register('task', TaskAnswerModelViewSet, 'task')

urlpatterns = [

]

urlpatterns += router.urls
