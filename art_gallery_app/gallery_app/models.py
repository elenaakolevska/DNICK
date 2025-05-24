from tkinter.constants import CASCADE

from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Artist(models.Model):
    name = models.CharField(max_length=15)
    country = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    biography = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.country}"
class Exhibition(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return f"{self.name} {self.description}"

class Artwork(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date = models.DateField()
    photo = models.ImageField(upload_to='art_app/', blank=True, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.description}"

