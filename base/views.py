from django.shortcuts import render , HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from rest_framework.generics import RetrieveAPIView , ListAPIView
from .utils import get_response
from datetime import datetime






class CalenderView(APIView):
    def post(self,request):
        longitude = request.data.get('longitude')
        latitude = request.data.get('latitude')
        day = request.data.get('day')
        month = request.data.get('month')
        year = request.data.get('year')

        response = get_response(longitude,latitude,day,month,year)
        gregorian_date = {
            'day': response['data']['date']['gregorian']['day'],
            'month': response['data']['date']['gregorian']['month']['en'],
            'year': response['data']['date']['gregorian']['year'],
        }

        hijri_date = {
                'day': response['data']['date']['hijri']['day'],
                'month': response['data']['date']['hijri']['month']['ar'],
                'year': response['data']['date']['hijri']['year'],
                'weekday': response['data']['date']['hijri']['weekday']['ar'],
            }

        gregorian = GregorianSerializer(gregorian_date)
        hijri = HijriSerializer(hijri_date)
        arabic_gregorian_date = gregorian.data
        arabic_hijri_date = hijri.data

        return Response({
            'timings': response['data']['timings'],
            'hijri' : arabic_hijri_date,
            'gregorian': arabic_gregorian_date,
            'city': response['data']['meta']['timezone']
        })
    
