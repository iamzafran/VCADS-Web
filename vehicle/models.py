from django.db import models

# Create your models here.


class VehicleMake(models.Model):
    vehicle_make = models.CharField(max_length=120)


class VehicleModel(models.Model):
    vehicle_model = models.CharField(max_length=120)


class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=120)


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)
    license_plate = models.CharField(max_length=20, unique=True)
