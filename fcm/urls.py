from django.urls import path
from fcm import views


urlpatterns = [
    path(
        '',
        views.first_view.as_view(extra_context={'fcm': 'active'}),
        name='fcm'
    ),
    path('test/', views.get_item, name='rackget')
]
