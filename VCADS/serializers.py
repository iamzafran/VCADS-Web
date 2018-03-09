from rest_framework import serializers
from user.models import User
from vehicle.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = '__all__'


class VehicleMakeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMake
        fields = '__all__'


class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = '__all__'


class VehicleSerializer(serializers.ModelSerializer):
    vehicle_type = VehicleTypeSerializer()
    vehicle_make = VehicleMakeSerializer()
    vehicle_model = VehicleModelSerializer()

    class Meta:
        model = Vehicle
        fields = '__all__'


