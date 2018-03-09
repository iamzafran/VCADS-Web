from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import HttpResponse
from .models import User

# Create your views here.


def index(request):
    return "user"


class AddUser(APIView):

    def get(self, request):
        return HttpResponse("add user")

    def post(self, request):
        data = request.data
        userUUID = data['uuid']
        u = User(uuid=userUUID)
        u.save()
        return HttpResponse("Ok")
