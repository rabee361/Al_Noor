from django.shortcuts import render , HttpResponse
from base.api.serializers import *
from base.models import *
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class CreatePilgrim(CreateAPIView):
    queryset = Pilgrim.objects.all()
    serializer_class = PilgrimSeriailzer




#####################################################################
class ListCreateTypeGuidance(ListCreateAPIView):
    queryset = TypeGuidance.objects.all()
    serializer_class = TypeGuidanceSerializer

class RetUptDelTypeGuidance(RetrieveUpdateDestroyAPIView):
    queryset = TypeGuidance.objects.all()
    serializer_class = TypeGuidanceSerializer

class ListCreateReligiousGuide(APIView):

    def post(self, request, pk):
        type_guidance = TypeGuidance.objects.filter(pk=pk).first()
        serializer = ReligiousGuideSerializer(data=request.data, context={'type_guidance':type_guidance})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, pk):
        type_guidance = TypeGuidance.objects.filter(pk=pk).first()
        religiousguide = type_guidance.religiousguide_set.all()
        serializer =ReligiousGuideSerializer(religiousguide, many=True)
        return Response(serializer.data)


class RetUptDelReligiousGuide(RetrieveUpdateDestroyAPIView):
    queryset = ReligiousGuide.objects.all()
    serializer_class = ReligiousGuideSerializer

class ListCreateTypeReligious(ListCreateAPIView):
    queryset = TypeReligious.objects.all()
    serializer_class = TypeReligiousSerializer

class RetUptDelTypeReligious(RetrieveUpdateDestroyAPIView):
    queryset = TypeReligious.objects.all()
    serializer_class = TypeReligiousSerializer

class ListCreateReligiousWorks(APIView):

    def post(self, request, pk):
        type_religious = TypeReligious.objects.filter(pk=pk).first()
        serializer = ReligiousWorksSerializer(data=request.data, context={'type_religious':type_religious})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        type_religious = TypeReligious.objects.filter(pk=pk).first()
        religiousworks = type_religious.religiousworks_set.all()
        serializer =ReligiousWorksSerializer(religiousworks, many=True)
        return Response(serializer.data)
    

class RetUptDelReligiousWorks(RetrieveUpdateDestroyAPIView):
    queryset = ReligiousWorks.objects.all()
    serializer_class = ReligiousWorksSerializer