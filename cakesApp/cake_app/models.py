from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Cake (models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='cake_photos/', null=True, blank=True)
    baker = models.ForeignKey('Baker', on_delete=models.CASCADE, null=True, blank=True, related_name='cakes')

    def __str__(self):
        return self.name

class Baker(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='bakers/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"