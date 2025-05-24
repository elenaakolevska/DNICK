from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class RealEstate(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    area = models.FloatField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='real_estate_photos/',   null=True, blank=True)
    is_reserved = models.BooleanField(null=True, blank= True)
    is_sold = models.BooleanField(null=True, blank= True)

    def __str__(self):
       return f"{self.name} {self.area} {self.location}"

class Agent(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    surname = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(max_length=250, null=True, blank=True)
    num_sales = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
       return f"{self.name} {self.surname}"



class RealEstateAgent(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, null=True, blank=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE, null=True, blank=True)

class Characteristics(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self):
       return f"{self.name}"

class CharacteristicsRealEstate(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE, null=True, blank=True)
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE, null=True, blank=True)
