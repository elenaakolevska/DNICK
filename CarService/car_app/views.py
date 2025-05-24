from django.shortcuts import render, redirect

from car_app import forms
from car_app.forms import ServiceForm
from car_app.models import Service


# Create your views here.
def index(request):
    return render(request, "index.html")

def repairs(request):

    if request.method == "POST":
        form_data = ServiceForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            repair = form_data.save(commit=False)
            repair.user = request.user
            repair.photo = form_data.cleaned_data["photo"]
            repair.save()
            return redirect("repairs")
    context = {
        "form": ServiceForm,
         "repairs": Service.objects.all()
    }
    # filter(user=request.user, car__type="Sedan")

    return render(request, 'repairs.html', context)