from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Course(models.Model):

    TYPE_CHOICES = [
        ("O", "Online"),
        ("P", "Physically")
    ]

    name=  models.CharField(max_length=100)
    description=  models.TextField(max_length=300, null=True, blank=True)
    photo=  models.ImageField(upload_to="course_photos/", blank=True, null=True)
    start_date=  models.DateField(null=True, blank=True)
    end_date=  models.DateField(null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES, null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

class Lecturer(models.Model):
    TYPE_CHOICES = [
        ("L", "Lecturer"),
        ("P", "Professor"),
        ("D", "Dr")
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, null=True, blank=True)
    academic_title = models.CharField(max_length=1, choices=TYPE_CHOICES, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    user =  models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class LecturerCourse(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.course} {self.lecturer}"