from django.shortcuts import render
from users.forms import CustomUserCreationForm
from django.views import generic
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from users.forms import CustomUserCreationForm


# Create your views here.
class register_view(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'users/register.html'
