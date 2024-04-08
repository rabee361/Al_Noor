from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUser():
    image = models.ImageField(upload_to='/accounts',default='')
    phonenumber = PhoneNumberField(region='SA',unique=True)



class Management(models.Model):
    pass


class Pilgrim():
    flight_num = models.IntegerField()
    flight_date = models.DateField()
    arrive = models.TimeField()
    departure = models.TimeField()
    duration = models.DurationField()
    gate_num = models.IntegerField()
    borading_time = models.TimeField()
    # flight_company = models.CharField(max_length=50) ### can be a choice list
    # company_logo = models.ImageField() in case of a company needed a logo
    status = models.BooleanField()
    hotel = models.CharField(max_length=100)
    # hotel_address = models.CharField(max_length=100) #### link to google maps can be long and lat
    room_num = models.IntegerField()



class Employee():
    pass



class Task(models.Model):
    body = models.CharField(max_length=500)
    content = models.CharField(max_length=100)
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)



class Guide():
    pass

class Notification():
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)


class Chat():
    pass

class ChatMessage():
    pass


