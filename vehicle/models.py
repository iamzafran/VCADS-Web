from django.db import models
from user.models import User

# Create your models here.


class VehicleMake(models.Model):
    vehicle_make = models.CharField(max_length=120)

    def __str__(self):
        return self.vehicle_make


class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=120)

    def __str__(self):
        return self.vehicle_type


class VehicleModel(models.Model):
    vehicle_model = models.CharField(max_length=120)
    vehicle_type = models.ForeignKey(VehicleType, on_delete=models.SET_NULL, null=True)
    vehicle_make = models.ForeignKey(VehicleMake, on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_model


class Vehicle(models.Model):
    vehicle_model = models.ForeignKey(VehicleModel, on_delete=models.SET_NULL, null=True)
    license_plate = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.license_plate
