from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Service(models.Model):
    code = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    description = models.TextField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='carService_photos/', null=True, blank=True)
    car = models.ForeignKey('Car', on_delete = models.CASCADE, null=True, blank=True)
    service_place = models.ForeignKey('ServicePlace', on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.code} {self.car}"

class Car(models.Model):

    CAR_TYPES = [
        ("A", "Jeep"),
        ("B", "SUV"),
        ("Sedan", "Sedan")
    ]

    type = models.CharField(max_length=10, choices=CAR_TYPES)
    manufacturer = models.ForeignKey('Manufacturer', on_delete = models.CASCADE, null=True, blank=True)
    speed = models.CharField(max_length=100)
    color = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.type} {self.speed}"

class ServicePlace(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    old_timer = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    owner_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class ServicePlaceManufacturer(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete = models.CASCADE, null=True, blank=True)
    service_place = models.ForeignKey(ServicePlace, on_delete = models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.manufacturer} {self.service_place}"


