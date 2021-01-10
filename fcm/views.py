from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy

from fcm.forms import RackForm, GetItem
from fcm.models import rack

# Create your views here.

class first_view(CreateView):
    form_class = RackForm
    success_url = reverse_lazy('fcm')
    template_name = 'fcm/first.html'


def get_item(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = GetItem(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            try:
                y = form.cleaned_data.get("your_id")
                x = rack.objects.filter(stored_items_owner=y)
                b = rack.objects.filter(stored_items_owner=y).values('cell_number')
                a = b.get()
                v = a.get('cell_number')
                v = "at {} cell".format(v)
                return render(request, 'fcm/third.html', context = {'data': v})
            except:
                return render(request, 'fcm/third.html', context = {'data': 'Not Found'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GetItem()

    return render(request, 'fcm/second.html', {'form': form})