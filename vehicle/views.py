from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from .models import VehicleModel, Vehicle
from user.models import User
from .serializers import VehicleModelSerializer, VehicleSerializer
# Create your views here.


def index(request):
    return "user"


def get_vehicle_models(request, model):
    query = model
    print(query)
    vehicle_model = VehicleModel.objects.filter(vehicle_model__icontains=query)
    serializer = VehicleModelSerializer(vehicle_model, many=True)

    return JsonResponse(serializer.data, safe=False)


class AddVehicleToUser(APIView):

    def get(self, request):
        return HttpResponse("add vehicle to user")

    def post(self, request):
        data = request.data
        uuid = data['uuid']
        model = int(data['model'])
        license_plate = data['license_plate']
        key = data['key']

        vehicle_model = VehicleModel.objects.get(id=model)
        user = User.objects.get(uuid=uuid)

        v = Vehicle(vehicle_model=vehicle_model, user=user, license_plate=license_plate, key=key)
        v.save()

        return HttpResponse("Vehicle added to user")


def get_user_vehicle(request, uuid):
    print(uuid)
    u = User.objects.get(uuid=uuid)
    v = Vehicle.objects.filter(user=u)

    serializer = VehicleSerializer(v, many=True)
    return JsonResponse(serializer.data, safe=False)


class DeleteVehicleFromUser(APIView):

    def get(self, request):
        return "Delete Vehicle"

    def post(self, request):
        data = request.data
        id = data['vehicle_id']

        vehicle = Vehicle.objects.get(id=id)
        vehicle.delete()

        return HttpResponse("OK")