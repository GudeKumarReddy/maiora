from django.urls import path, include
from rest_framework import routers

from tasks.views import TaskViewSet, TaskDetailViewSet

router = routers.DefaultRouter()
router.register('task', TaskViewSet)
router.register('task-detail', TaskDetailViewSet)

urlpatterns = [
    path('', include(router.urls))
]
