from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from .models import VehicleModel
from .serializers import VehicleModelSerializer
# Create your views here.


def index(request):
    return "user"


def get_vehicle_models(request, model):
    query = model
    print(query)
    vehicle_model = VehicleModel.objects.filter(vehicle_model__icontains=query)
    serializer = VehicleModelSerializer(vehicle_model, many=True)

    return JsonResponse(serializer.data, safe=False)
