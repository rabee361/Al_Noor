from typing import Iterable
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from .options import *
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):
    username = models.CharField(max_length=50)
    image = models.ImageField(upload_to='accounts',default='')
    phonenumber = PhoneNumberField(region='SA',unique=True)
    email = models.EmailField(null=True, blank=True)

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ('username',)


    def __str__(self) -> str:
        return self.username

# class Management(models.Model):
#     pass

class Pilgrim(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    flight_num = models.IntegerField(null=True, blank=True)
    flight_date = models.DateField(null=True, blank=True)
    # arrive = models.TimeField()
    # departure = models.TimeField()
    # duration = models.DurationField()
    gate_num = models.IntegerField(null=True, blank=True)
    # borading_time = models.TimeField()
    # flight_company = models.CharField(max_length=50) ### can be a choice list
    # company_logo = models.ImageField() in case of a company needed a logo
    status = models.BooleanField(null=True, blank=True)
    hotel = models.CharField(max_length=100, null=True, blank=True)
    # hotel_address = models.CharField(max_length=100) #### link to google maps can be long and lat
    room_num = models.IntegerField(null=True, blank=True)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    grand_father = models.CharField(max_length=50)
    family_name = models.CharField(max_length=50)
    identification_number = models.IntegerField()
    birthday = models.DateField()
    phonenumber = PhoneNumberField(region='SA',unique=True)
    job_position = models.CharField(choices=Job_position, max_length=50, null=True, blank=True)
    gender = models.CharField(choices=Gender, max_length=10)
    options_trip = models.CharField(choices=Options_trip, max_length=20)
    marital_status = models.CharField(choices=Marital_status, max_length=10)
    address = models.CharField(choices=Address, max_length=15)
    type_alhajj = models.CharField(choices=Type_alhajj, max_length=50, null=True, blank=True)
    tradition_reference = models.CharField(choices=Tradition_reference)
    count_hajjas = models.BigIntegerField(null=True, blank=True)
    last_year = models.CharField(null=True, blank=True)
    means_journey = models.CharField(choices=Means_journey, max_length=50)
    blood_type = models.CharField(choices=Blood_type, null=True, blank=True)
    are_sick = models.BooleanField(null=True, blank=True)
    chronic_diseases = models.CharField(null=True, blank=True, max_length=200)
    tawaf = models.BooleanField(null=True, blank=True)
    sai = models.BooleanField(null=True, blank=True)
    wheelchair = models.BooleanField(null=True, blank=True)
    type_help = models.TextField(null=True, blank=True)
    imported = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.first_name} - {self.family_name}'

class Employee():
    employee = models.OneToOneField(CustomUser, on_delete=models.CASCADE)



# class Task(models.Model):
#     body = models.CharField(max_length=500)
#     content = models.CharField(max_length=100)
#     employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
#     created = models.DateTimeField(auto_now_add=True)
#     completed = models.BooleanField(default=False)



# class Guide():
#     pass

# class Notification():
#     title = models.CharField(max_length=50)
#     content = models.CharField(max_length=200)
#     created = models.DateTimeField(auto_now_add=True)



class Chat(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    type_chat = models.CharField(choices=Type_user)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username}-type-chat {self.type_chat}'


class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat , on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} : "{self.content[0:20]}..."'

    class Meta:
        ordering=['-timestamp']

##########################################################
class TypeGuidance(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class ReligiousGuide(models.Model):
    type_guidance = models.ForeignKey(TypeGuidance, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='guidance')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        print('my name is jacoub')
    
    class Meta:
        ordering = ['created_at']

class TypeReligious(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class ReligiousWorks(models.Model):
    type_religious = models.ForeignKey(TypeReligious, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='religious')
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
        
    # for senf notivecation for user
    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        print('my name is jacoub')

    
    class Meta:
        ordering = ['created_at']