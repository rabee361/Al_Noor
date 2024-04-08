from django.db import models


class CustomUser():
    pass

class Task(models.Model):
    body = models.CharField(max_length=500)
    content = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)


class Management(models.Model):
    pass

class Pilgrim():
    flight_num = models.IntegerField()
    hotel = models.CharField(max_length=100)
    hotel_address = models.CharField(max_length=100)
    room_num = models.IntegerField()


class Employee():
    pass

class Guide():
    pass

class Notification():
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)

class Chat():
    pass

class ChatMessage():
    pass

class Chat():
    pass

class Chat():
    pass

