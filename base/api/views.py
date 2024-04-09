from django.shortcuts import render , HttpResponse
from base.api.serializers import *
from base.models import *
from rest_framework.generics import CreateAPIView

class CreatePilgrim(CreateAPIView):
    queryset = Pilgrim.objects.all()
    serializer_class = PilgrimSeriailzer

