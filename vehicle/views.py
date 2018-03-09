from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return "user"


class VehicleModelAutoComplete(APIView):

    def get(self, request):
        return HttpResponse("Vehicle Model AutoComplete")
