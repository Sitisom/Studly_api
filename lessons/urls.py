from rest_framework import routers

from lessons.views import AssignmentsViewSet, TaskAnswerModelViewSet

router = routers.DefaultRouter()

router.register('assignments', AssignmentsViewSet, 'assignments')
router.register('task', TaskAnswerModelViewSet, 'task')

urlpatterns = []

urlpatterns += router.urls
