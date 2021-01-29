from django.urls import path
from tasks import views

urlpatterns = [
    path(
        '',
        views.Tasksview.as_view(
            extra_context={'tasks': 'active'},
            ),
        name='tasks'
    ),
    path(
        'table',
        views.TasksTabview.as_view(),
        name='tabletask'
    ),
]