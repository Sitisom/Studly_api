from rest_framework import routers

from lessons.views import AssignmentsViewSet, TaskAnswerModelViewSet, LessonViewSet

router = routers.DefaultRouter()

router.register('', LessonViewSet, 'lessons')
router.register('assignments', AssignmentsViewSet, 'assignments')
router.register('task', TaskAnswerModelViewSet, 'task')

urlpatterns = []

urlpatterns += router.urls
