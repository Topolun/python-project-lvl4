from django.urls import path
from users import views


urlpatterns = [
    path(
        'login/',
        views.CustomLoginView.as_view(
            template_name='users/login.html',
            extra_context={'login': 'active'},
            ),
        name='login'
    ),
    path(
        'logout/',
        views.logout_view.as_view(),
        name='logout'
    ),
    path(
        'create/',
        views.register_view.as_view(
            extra_context={'register': 'active'},
            http_method_names=['get', 'post']
            ),
        name='CreateUser'
    ),
    path(
        '',
        views.users_list_view.as_view(),
        name='userlist'
    ),
    path(
        '<int:pk>/update/',
        views.change_view.as_view(
            extra_context={'users': 'active'},
            http_method_names=['get', 'post']
            ),
        name='UpdateUser'
    ),
    path(
        '<int:pk>/delete/',
        views.delete_view.as_view(extra_context={'users': 'active'}),
        name='DeleteUser'
    ),
]
