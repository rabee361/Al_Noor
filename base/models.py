from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .utils import *
from .options import *
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/users',default='images/account.jpg')
    phonenumber = PhoneNumberField(region='SA',unique=True)
    is_verified = models.BooleanField(default=False)
    get_notifications = models.BooleanField(default=True)

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ('username',)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = _("User")
        verbose_name_plural = _("Users")
   



class VerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    code = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=get_expiration_time)

    def __str__(self):
        return f'{self.user.username} code:{self.code}'


# # in case we needed to store the hotel info in a seperate model
# # class Hotel():
# #     pass



class Management(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']



class Registration(models.Model):
    phonenumber = PhoneNumberField(region='SA',unique=True)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    grand_father = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_number = models.IntegerField()
    birthday = models.DateField()
    job_position = models.CharField(choices=Job_position, max_length=50, null=True, blank=True)
    gender = models.CharField(choices=Gender, max_length=10)
    options_trip = models.CharField(choices=Options_trip, max_length=20)
    marital_status = models.CharField(choices=Marital_status, max_length=10)
    address = models.CharField(choices=Address, max_length=15)
    alhajj = models.CharField(choices=Type_alhajj, max_length=50, null=True, blank=True)
    tradition_reference = models.CharField(choices=Tradition_reference)
    count_hajjas = models.BigIntegerField(null=True, blank=True)
    last_year = models.CharField(null=True, blank=True)
    means_journey = models.CharField(choices=Means_journey, max_length=50)
    blood_type = models.CharField(choices=Blood_type, null=True, blank=True)
    illness = models.BooleanField(null=True, blank=True)
    chronic_diseases = models.CharField(null=True, blank=True, max_length=200)
    tawaf = models.BooleanField(null=True, blank=True)
    sai = models.BooleanField(null=True, blank=True)
    wheelchair = models.BooleanField(null=True, blank=True)
    type_help = models.TextField(null=True, blank=True)



class Pilgrim(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , default=1)
    registeration_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    grand_father = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    phonenumber = PhoneNumberField(region='SA',unique=True)
    flight_num = models.IntegerField(null=True, blank=True,verbose_name="رقم الرحلة")
    arrival = models.DateTimeField()
    departure = models.DateTimeField()
    duration = models.DurationField()
    borading_time = models.TimeField()####
    gate_num = models.IntegerField(null=True, blank=True)####
    flight_company = models.CharField(max_length=50) ### can be a choice list
    company_logo = models.ImageField() ###
    status = models.BooleanField(null=True, blank=True)
    hotel = models.CharField(max_length=100, null=True, blank=True)
    hotel_address = models.CharField(max_length=100) #### link to google maps can be long and lat
    room_num = models.IntegerField(null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.id} - {self.id}'



class Guide(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE ,default=1)
    
    def __str__(self) -> str:
        return self.user.username



class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']




class Task(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    title = models.CharField(max_length=500,unique=True)
    content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.employee.user.username} : {self.title}'




class UserNotification(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} : {self.content}'


class Note(models.Model):
    pilgrim = models.ForeignKey(Pilgrim,on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide,on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.pilgrim.user.username} : {self.content}'



class Chat(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} chat'


class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat , on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
    employee = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.sender} : "{self.content[0:20]}..."'

    class Meta:
        ordering=['-timestamp']



class GuidanceCategory(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self) -> str:
        return self.name



class GuidancePost(models.Model):
    category = models.ForeignKey(GuidanceCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(upload_to='cover')
    created = models.DateField(auto_now_add=True) ##datetime ??

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-created']




class ReligiousCategory(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
    

class ReligiousPost(models.Model):
    category = models.ForeignKey(ReligiousCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    cover = models.ImageField(upload_to='cover')
    created = models.DateField(auto_now_add=True)## datetime ?

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created']
