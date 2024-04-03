from django.db import models
from django.contrib.auth.models import User

PRIORITY = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
)


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    priority = models.CharField(max_length=20, choices=PRIORITY, default='medium')

    def __str__(self):
        return self.title


class TaskDetail(models.Model):
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name='detail')
    assigned_to = models.ManyToManyField(User, null=True, blank=True)

    def __str__(self):
        return self.task.title
