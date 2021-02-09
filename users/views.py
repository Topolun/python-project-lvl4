from django.shortcuts import render
from users.forms import CustomUserCreationForm
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


# Create your views here.
class register_view(SuccessMessageMixin, CreateView):
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    success_message = 'User was created sucsessefully'


class users_list_view(ListView):
    model = CustomUser
    paginate_by = 10
    template_name = 'users/userlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields_to_use = ['id', 'username', 'get_full_name()', 'date_joined']
        context['columns'] = fields_to_use
        context['users'] = 'active'
        return context


class change_view(SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('login')
    not_success_url = reverse_lazy('userlist')
    template_name = 'users/update.html'
    success_message = 'User data was changed sucsessefully'
    not_success_message = 'Please log in as user'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        obj = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.object.pk is not request.user.pk:
            redirect_to = self.not_success_url
            messages.warning(self.request, self.not_success_message % obj.__dict__)
            return HttpResponseRedirect(redirect_to)
        return self.render_to_response(context)


class delete_view(SuccessMessageMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('userlist')
    template_name = 'users/delete.html'
    success_message = 'User was deleted sucsessefully'
    not_success_message = 'Please log in as user'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        obj = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.object.pk is not request.user.pk:
            success_url = self.get_success_url()
            messages.warning(self.request, self.not_success_message % obj.__dict__)
            return HttpResponseRedirect(success_url)
        return self.render_to_response(context)


    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        data_to_return = super(delete_view, self).delete(request, *args, **kwargs)
        messages.success(self.request, self.success_message % obj.__dict__)
        return data_to_return

