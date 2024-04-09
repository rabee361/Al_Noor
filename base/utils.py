from datetime import datetime
import requests
from rest_framework.response import Response
from datetime import datetime , timedelta 
from django.utils import timezone
import random

weekday_mapping = {
    'Monday': 'الاثنين',
    'Tuesday': 'الثلاثاء',
    'Wednesday': 'الأربعاء',
    'Thursday': 'الخميس',
    'Friday': 'الجمعة',
    'Saturday': 'السبت',
    'Sunday': 'الأحد'
}




def get_response(longitude,latitude,day,month,year):
    Url = 'http://api.aladhan.com/v1/timings/'
    formatted_date = ''
    if day and month and year:
        date = datetime(int(year), int(month), int(day))
        formatted_date = date.strftime("%d-%m-%Y")
        print(Url+formatted_date)
    else:
        return Response({"error":"wrong data"})
    
    p = {
        'longitude' : longitude,
        'latitude' : latitude
    }
    response = requests.get(Url+formatted_date,params=p)
    return response.json()




def get_expiration_time():
    return timezone.now() + timedelta(minutes=10)



def generate_code():
    code_verivecation = random.randint(1000,9999)
    return code_verivecation
