from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView

from tasks.forms import TasksForm
from tasks.models import Tasks


class Tasksview(CreateView):
    form_class = TasksForm
    success_url = reverse_lazy('home')
    template_name = 'tasks/tasks.html'


class TasksTabview(ListView):
    model = Tasks
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        b = Tasks._meta.get_fields()
        c = []
        for i in b:
            i = str(i)
            c.append(i.rpartition('.')[2])
        context['test'] = c
        context['proba'] = {'Ключ': 'Значение'}
        context['fields'] = 'i.name'
        return context
