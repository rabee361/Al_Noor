from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator , RegexValidator
from .utils.utils import *
from .utils.options import *
from django.utils.translation import gettext_lazy as _
from .utils.managers import GuideChats , ManagerChats , CustomManager



class CustomUser(AbstractUser):
    USER_TYPES = (
        ('حاج' , 'حاج'),
        ('مرشد' , 'مرشد'),
        ('اداري' , 'اداري'),
        ('موظف' , 'موظف'),
    )
        
    image = models.ImageField(upload_to='images/users',default='images/account.jpg')
    phonenumber = models.CharField(unique=True,
                                   db_index=True,
                                            validators=[RegexValidator(
                                            regex=r'^\d{5,15}$'
                                        )])
    is_verified = models.BooleanField(default=False)
    get_notifications = models.BooleanField(default=True)
    username = models.CharField(max_length=255)
    user_type = models.CharField(max_length=30 , choices=USER_TYPES , null=True , blank=True)
    active_now = models.BooleanField(default=False)

    # objects = CustomManager()

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ('username',)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-id']

   







class VerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    code = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=get_expiration_time)

    def __str__(self):
        return f'{self.user.username} code:{self.code}'



class Management(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']


class Registration(models.Model):
    phonenumber = models.CharField(unique=True,
                                        validators=[RegexValidator(
                                        regex=r'^\d{5,15}$'
                                    )])
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
    tradition_reference = models.CharField()
    count_hajjas = models.BigIntegerField(null=True, blank=True)
    last_year = models.CharField(null=True, blank=True)
    means_journey = models.CharField(choices=Means_journey, max_length=50)
    blood_type = models.CharField(choices=Blood_type, null=True, blank=True)
    illness = models.BooleanField(null=True, blank=True)
    tawaf = models.BooleanField(null=True, blank=True)
    sai = models.BooleanField(null=True, blank=True)
    wheelchair = models.BooleanField(null=True, blank=True)
    type_help = models.CharField(max_length=500,null=True, blank=True)




class Pilgrim(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    phonenumber = models.CharField(unique=True,
                                    db_index=True,
                                            validators=[RegexValidator(
                                            regex=r'^\d{5,15}$'
                                        )])
    longitude = models.FloatField(max_length=100,default=24.3) 
    latitude = models.FloatField(max_length=100,default=45.2)
    registeration_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    grand_father = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField(null=True , blank=True)
    flight_num = models.IntegerField(null=True, blank=True)
    flight_date = models.DateField(null=True, blank=True)
    arrival = models.TimeField(null=True , blank=True)
    departure = models.TimeField(null=True , blank=True)
    from_city = models.CharField(max_length=40 , null=True , blank=True)
    to_city = models.CharField(max_length=40 , null=True , blank=True)
    duration = models.CharField(max_length=40,null=True,blank=True)
    boarding_time = models.TimeField(null=True , blank=True)
    gate_num = models.IntegerField(null=True, blank=True)
    flight_company = models.CharField(max_length=50)
    company_logo = models.ImageField(null=True , blank=True,default='images/account.jpg')
    status = models.BooleanField(null=True, blank=True)
    hotel = models.CharField(max_length=100, null=True, blank=True)
    hotel_address = models.CharField(max_length=100)
    room_num = models.IntegerField(null=True, blank=True)
    haj_steps = models.ManyToManyField('HajSteps' , blank=True, through='HaJStepsPilgrim')
    guide = models.ForeignKey('Guide' ,null=True , blank=True , on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f'{self.user.username}'

    @property
    def last_step(self):
        return self.haj_steps.all().last()

    @property
    def guide_chat(self):
        try:
            guide_chat = Chat.objects.get(user=self.user , chat_type='guide')
            return guide_chat.id
        except Chat.DoesNotExist:
            return None 

    @property
    def manager_chat(self):
        try:
            guide_chat = Chat.objects.get(user=self.user , chat_type='guide')
            return guide_chat.id
        except Chat.DoesNotExist:
            return None 





class Guide(models.Model):
    user = models.OneToOneField(CustomUser , on_delete=models.CASCADE ,default=1)
    
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
    accepted = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.employee.user.username} : {self.title}'



class UserNotification(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    info = models.CharField(max_length=200 , null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} : {self.content}'
    


class BaseNotification(models.Model):
    sentBy = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title




class Note(models.Model):
    pilgrim = models.ForeignKey(Pilgrim,on_delete=models.CASCADE)
    guide = models.ForeignKey(Guide,on_delete=models.CASCADE)
    content = models.CharField(max_length=500 ,null=True, blank=True)
    audio = models.FileField(upload_to='audio/pilgrims' , null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.pilgrim.user.username} : note'






class Chat(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    chat_type = models.CharField(choices=CHAT_CHOICES, max_length=20 , default='guide')

    objects = models.Manager()
    guide_chats = GuideChats()
    manager_chats = ManagerChats()

    def __str__(self) -> str:
        return f'{self.user.username} chat'




class AudioAttach(models.Model):
    file = models.FileField(upload_to='audio/chats') # to send audio record in chat




class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser , on_delete=models.CASCADE ,blank=True,null=True)
    chat = models.ForeignKey(Chat , on_delete=models.CASCADE)
    content = models.CharField(max_length=500 ,null=True)
    audio = models.ForeignKey(AudioAttach , on_delete=models.CASCADE , null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False) # to see if the user read the message or not
    sent_user = models.BooleanField(default=False)

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
    rank = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(1000)])
    created = models.DateField(auto_now_add=True) # datetime ?

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['rank']



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
    rank = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(1000)])
    created = models.DateField(auto_now_add=True) # datetime ?

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['rank']



class SecondarySteps(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    note = models.CharField(max_length=500,default='note')

    def __str__(self) -> str:
        return self.name
    




class HajSteps(models.Model):
    name = models.CharField(max_length=50)
    rank = models.IntegerField(blank=True , null=True , validators=[MinValueValidator(1),MaxValueValidator(1000)])
    secondary_steps = models.ManyToManyField(SecondarySteps)
    note = models.CharField(max_length=500,default='note')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['rank']







class HaJStepsPilgrim(models.Model):
    pilgrim = models.ForeignKey(Pilgrim, on_delete=models.CASCADE)
    haj_step = models.ForeignKey(HajSteps, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pilgrim.user.username}: {self.haj_step.name}"






class UserPassword(models.Model):
    username = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

