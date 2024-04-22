# core/models.py

from django.db import models
from django.contrib.auth.models import User
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_station = models.CharField(max_length=100)
    destination_station = models.CharField(max_length=100)
    date = models.DateField()
    passenger_name = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.passenger_name}'s Ticket from {self.departure_station} to {self.destination_station}"

class Station(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Train(models.Model):
    trainTitle = models.CharField(max_length=200)
    deptTiming = models.CharField(max_length=10)
    deptStation = models.CharField(max_length=100)
    deptDate = models.CharField(max_length=20)
    desTiming = models.CharField(max_length=10)
    desStation = models.CharField(max_length=100)
    desDate = models.CharField(max_length=20)

    def __str__(self):
        return self.trainTitle