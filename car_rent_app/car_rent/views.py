from gc import get_objects

from django.shortcuts import render, get_object_or_404
from .models import   *

# Create your views here.

def index(request):
    cars = Car.objects.all()
    context = {'car_list': cars, 'app_name': 'car_rent'}
    return render(request, 'index.html', context)

def details(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {'car_data': car, 'app_name': 'car_rent'}
    return render(request, 'details.html', context)