from django.db import models
from django.utils import timezone

# Create your models here.

class Bin(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.FloatField(default=32.32)
    longitude = models.FloatField(default=33.33)
    collection_frequency = models.IntegerField(default=1)
    last_collection = models.DateTimeField(default=timezone.now)

#class Vehicle(models.Model):
#    id = models.IntegerField(primary_key=True)
#    plate = models.CharField(max_length=20, default='00 ABC 99')

class Operation(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, default='collect')
    bin = models.ForeignKey(Bin, on_delete=models.CASCADE, default=1)
    #vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=1)