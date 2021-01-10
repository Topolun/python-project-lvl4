from django.shortcuts import render


def index(request):
    return render(
        request,
        'task_manager/index.html',
        context = {'who': 'dear friend', 'home': 'active'},
        )
