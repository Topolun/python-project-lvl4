from django.urls import path
from django.contrib.auth import views as authviews
from users import views


urlpatterns = [
    path(
        'login/',
        authviews.LoginView.as_view(
            template_name='users/login.html',
            extra_context={'login': 'active'},
            ),
        name='login'
    ),
    path(
        'logout/',
        authviews.LogoutView.as_view(template_name='users/logout.html'),
        name='logout'
    ),
    path(
        'register/',
        views.register_view.as_view(extra_context={'register': 'active'}),
        name='CreateUser'
    )
]
