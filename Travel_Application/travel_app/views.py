from django.shortcuts import render, redirect

from travel_app.forms import TravelForm
from travel_app.models import Travel


# Create your views here.

def index(request):
    travels = Travel.objects.filter(duration__gt=3)
    context = {'travel_list': travels, 'app_name': 'travel_app'}
    return  render(request, 'index.html', context)

def add_travel(request):
    if request.method == 'POST':
        form = TravelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')
    form = TravelForm()
    return render(request, 'add_travel.html', context={'form': form})