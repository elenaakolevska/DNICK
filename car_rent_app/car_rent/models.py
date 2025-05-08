from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    year_establishment = models.CharField(max_length=4)
    num_employees = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):

    TYPE_CHOICES = [
        ("S", "Sedan"),
        ("SUV", "SUV"),
        ("H", "Hatchback"),
        ("C", "Coupe"),
    ]

    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    chassis_num = models.IntegerField()
    car_model = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    year_of_production = models.CharField(max_length=4)
    mileage = models.DecimalField(max_digits=10, decimal_places=2)
    car_type = models.CharField(max_length=3, choices=TYPE_CHOICES)
    photo = models.ImageField(upload_to="car_photos/", null=True, blank=True)

    def __str__(self):
        return f"{self.car_model} {self.manufacturer.name}"


