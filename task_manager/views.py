from django.shortcuts import render
from django.utils.translation import gettext as _


def index(request):
    output = _("Translate it")
    return render(
        request,
        'task_manager/index.html',
        context={'who': output, 'home': 'active'},
        )
