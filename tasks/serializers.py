from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task, TaskDetail


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskDetailSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)
    task_id = serializers.PrimaryKeyRelatedField(
        queryset=Task.objects.all(), source='task', write_only=True, required=False)
    class Meta:
        model = TaskDetail
        fields = '__all__'
