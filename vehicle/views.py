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


class VehicleModelAutoComplete(APIView):

    def get(self, request):
        print(request.data)
        string = "per"
        vehicle_model = VehicleModel.objects.filter(vehicle_model__icontains=string)
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        return Response(serializer.data)
