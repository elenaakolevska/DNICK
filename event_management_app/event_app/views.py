from turtledemo.clock import datum

from django.shortcuts import render, redirect, get_object_or_404

from event_app.forms import EventForm
from event_app.models import Event


# Create your views here.


def index(request):
    # events = Event.objects.filter(user = request.user)
    events = Event.objects.all()
    context = {'event_list': events, 'app_name': 'event_App'}
    return render(request, 'index.html', context)

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = EventForm()
    return render(request, "add-event.html", context={'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    # Flight.objects.filter(pk=flight_id).exists()

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()

        return redirect('index')

    form = EventForm(instance=event)
    return render(request, "edit-event.html", context={'form': form, 'event_id': event_id})