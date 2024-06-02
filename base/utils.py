from datetime import datetime
import requests
from rest_framework.response import Response
from datetime import datetime , timedelta 
from django.utils import timezone
import random
import secrets
import string


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
    Url = 'http://api.aladhan.com/v1/timings?tune=0,7,0,0,0,0,0,0,0'
    formatted_date = ''
    if day and month and year:
        date = datetime(int(year), int(month), int(day))
        formatted_date = date.strftime("%d-%m-%Y")
        print(Url+formatted_date)
    else:
        return Response({"error":"wrong data"})
    
    p = {
        'longitude' : longitude,
        'latitude' : latitude,
        'method' : 8,
    }
    response = requests.get(Url+formatted_date,params=p)
    return response.json()






def get_next_prayer(prayers,time):
    Fajr = prayers['Fajr']
    Sunrise = prayers['Sunrise']
    Dhuhr = prayers['Dhuhr']
    Asr = prayers['Asr']
    Maghrib = prayers['Maghrib']
    Isha = prayers['Isha']
    Time = datetime.strptime(time, "%H:%M").time()
    Fajr_time = datetime.strptime(Fajr, "%H:%M").time()
    Sunrise_time = datetime.strptime(Sunrise, "%H:%M").time()
    Dhuhr_time = datetime.strptime(Dhuhr, "%H:%M").time()
    Asr_time = datetime.strptime(Asr, "%H:%M").time()
    Maghrib_time = datetime.strptime(Maghrib, "%H:%M").time()
    Isha_time = datetime.strptime(Isha, "%H:%M").time()

    next_prayer_time = None
    for prayer_time in [Fajr_time, Sunrise_time, Dhuhr_time, Asr_time, Maghrib_time, Isha_time]:
        if prayer_time > Time:
            next_prayer_time = prayer_time
            break

    if next_prayer_time == None:
        next_prayer_time = Fajr_time

    return next_prayer_time



def get_expiration_time():
    return timezone.now() + timedelta(minutes=10)



def generate_code():
    code_verivecation = random.randint(1000,9999)
    return code_verivecation



def generate_password(length=10) -> str:
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    return password