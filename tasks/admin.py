from django.contrib import admin
from tasks.models import Tasks, TaskStatus, Tag


# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'creator', 'assigned_to')


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class TaskStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


admin.site.register(Tasks, TasksAdmin)
admin.site.register(TaskStatus, TaskStatusAdmin)
admin.site.register(Tag, TagAdmin)
