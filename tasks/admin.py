from django.contrib import admin

from tasks.models import Task, TaskDetail


class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'due_date', 'priority')


admin.site.register(Task, TasksAdmin)


# class TaskDetailAdmin(admin.ModelAdmin):
#     list_display = ('task', 'assigned_to')
#
#
admin.site.register(TaskDetail)
