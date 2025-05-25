from django.contrib.auth.models import User
from django.db import models


class Reservation(models.Model):
    code = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    room = models.ForeignKey('Room', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    photo = models.ImageField(upload_to='reservations/', null=True, blank=True)
    if_confirmed = models.BooleanField(null=True, blank=True)
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'type':'R'})

    def __str__(self):
        return f"{self.code}"

class Employee(models.Model):
    TYPE_CHOICES = [
        ("H", "Hygienist"),
        ("R", "Receptionist"),
        ("M", "Manager"),
    ]

    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

class Room(models.Model):

    number = models.IntegerField(null=True, blank=True)
    beds = models.IntegerField(null=True, blank=True)
    has_terrace = models.BooleanField(null=True, blank=True)
    is_cleaned = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.number}"

class RoomEmployee(models.Model):

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, limit_choices_to={'type':'H'})
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.employee} {self.room}"