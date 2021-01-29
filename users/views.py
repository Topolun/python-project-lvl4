from django.shortcuts import render
from users.forms import CustomUserCreationForm
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.list import ListView

from users.forms import CustomUserCreationForm
from users.models import CustomUser


# Create your views here.
class register_view(CreateView):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'

class users_list_view(ListView):
    model = CustomUser
    paginate_by = 10
    template_name = 'users/userlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        columns_to_use = ['id', 'username', 'get_full_name()', 'date_joined']
        columns = []
        for field in CustomUser._meta.get_fields():
            field = str(field)
            field = field.rpartition('.')[2]
            if field in columns_to_use:
                columns.append(field)
        context['columns'] = columns_to_use
        return context
