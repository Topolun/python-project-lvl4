from users.forms import CustomUserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.utils.translation import gettext_lazy as _

from users.forms import CustomUserChangeForm, CustomLoginForm
from users.models import CustomUser

from django.contrib.auth import views as authviews

# Custom Mixins:


class ErrorMessageMixin:
    error_message = ''

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        obj = self.get_object()
        context = self.get_context_data(object=self.object)
        if self.object.pk is not request.user.pk:
            redirect_to = self.unsuccesseful_url
            messages.error(self.request, self.error_message % obj.__dict__)
            return HttpResponseRedirect(redirect_to)
        return self.render_to_response(context)


# Create your views here.
class register_view(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/register.html'
    success_message = _('User "%(username)s" was created sucsessefully')


class users_list_view(ListView):
    model = CustomUser
    paginate_by = 5
    template_name = 'users/userlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fields_to_use = ['id', 'username', 'get_full_name()', 'date_joined']
        context['columns'] = fields_to_use
        context['users'] = 'active'
        return context


class change_view(ErrorMessageMixin, SuccessMessageMixin, UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('userlist')
    absolute_url = 'users/login.html'
    unsuccesseful_url = reverse_lazy('userlist')
    template_name = 'users/update.html'
    success_message = _(
        "%(username)s's data was changed sucsessefully"
        )
    error_message = _(
        'You can manage only your own data. Please log in as user "%(username)s"'  # noqa: E501
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class delete_view(ErrorMessageMixin, SuccessMessageMixin, DeleteView):
    model = CustomUser
    success_url = reverse_lazy('userlist')
    unsuccesseful_url = reverse_lazy('userlist')
    template_name = 'users/delete.html'
    success_message = _('User %(username)s was deleted sucsessefully')
    error_message = _('Please log in as user %(username)s')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        data_to_return = super(delete_view, self).delete(
            request, *args, **kwargs
            )
        messages.success(self.request, self.success_message % obj.__dict__)
        return data_to_return


class logout_view(authviews.LogoutView):
    success_message = _('Successfully logged out.')
    next_page = '/users/login'

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.success(request, self.success_message)
        return response


class CustomLoginView(authviews.LoginView):
    form_class = CustomLoginForm
