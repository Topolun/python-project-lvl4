from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from tasks.forms import TasksForm
from tasks.models import Tasks

# Create your views here.
class Tasksview(CreateView):
    form_class = TasksForm
    success_url = reverse_lazy('home')
    template_name = 'tasks/tasks.html'