from rest_framework import serializers
from .models import *


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMake
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer()
    vehicle_make = VehicleMakeSerializer()

    class Meta:
        model = VehicleModel
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):

    vehicle_model = VehicleModelSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'
