from django.shortcuts import render , HttpResponse
from .serializers import *
from .models import *
from rest_framework.generics import CreateAPIView

class CreatePilgrim(CreateAPIView):
    queryset = Pilgrim.objects.all()
    serializer_class = PilgrimSeriailzer

