from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class PublishingHouse(models.Model):

    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    website = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.country}"


class Book(models.Model):
    TYPE_CHOICES = [
    ("S", "Soft"),
    ("H", "Hard"),
    ]

    CATEGORY_CHOICES = [
    ("R", "Romance"),
    ("T", "Thriller"),
    ("B", "Biography"),
    ("C", "Classic"),
    ("D", "Drama"),
    ("H", "History"),
    ]

    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="book_photos/", blank=True, null=True)
    ISBN = models.CharField(max_length=50)
    year_published = models.IntegerField()
    num_of_pages = models.IntegerField()
    dimensions = models.CharField(max_length=20)
    cover_type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    price = models.IntegerField()
    publishing_house = models.ForeignKey(PublishingHouse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} {self.ISBN}"
