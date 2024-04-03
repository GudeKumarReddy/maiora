from rest_framework import viewsets
from .models import Task, TaskDetail
from .serializers import TaskSerializer, TaskDetailSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailViewSet(viewsets.ModelViewSet):
    queryset = TaskDetail.objects.all()
    serializer_class = TaskDetailSerializer
