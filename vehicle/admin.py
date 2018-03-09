from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Vehicle)
admin.site.register(models.VehicleModel)
admin.site.register(models.VehicleMake)
admin.site.register(models.VehicleType)
