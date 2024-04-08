from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/users',default='images/account.jpg')
    phonenumber = PhoneNumberField(region='SA',unique=True)

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ('username',)

    def __str__(self) -> str:
        return self.username







# # in case we needed to store the hotel info in a seperate model
# # class Hotel():
# #     pass



class Management(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username



class Pilgrim(models.Model):
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



class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username




class Task(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    content = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.employee.user.username} : {self.title}'



class Guide(models.Model):
    pass
    



class Notification(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
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

    def __str__(self):
        return f'{self.sender} : "{self.content[0:20]}..."'

    class Meta:
        ordering=['-timestamp']



