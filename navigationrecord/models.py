from evrekaDjangoProject.settings import USE_TZ
from django.db import models
from django.utils import timezone

# Create your models here.

class Vehicle(models.Model):
    id = models.IntegerField(primary_key=True)
    plate = models.CharField(max_length=15, default='00 ABC 99')


class NavigationRecord(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, default=1)
    datetime = models.DateTimeField(default=timezone.now)
    latitude = models.FloatField(default=32.32)
    longitude = models.FloatField(default=33.33)