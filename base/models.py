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
        
    image = models.ImageField(upload_to='images/users', default='images/users/account.jpg', verbose_name='الصورة')
    phonenumber = models.CharField(unique=True,
                                   db_index=True,
                                            validators=[RegexValidator(
                                            regex=r'^\d{5,15}$'
                                        )], verbose_name='رقم الهاتف')
    is_verified = models.BooleanField(default=False, verbose_name='تم التحقق')
    get_notifications = models.BooleanField(default=True, verbose_name='تلقي الإشعارات')
    username = models.CharField(max_length=255, verbose_name='اسم المستخدم')
    user_type = models.CharField(max_length=30, choices=USER_TYPES, null=True, blank=True, verbose_name='نوع المستخدم')
    active_now = models.BooleanField(default=False, verbose_name='نشط الآن')

    # objects = CustomManager()

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ('username',)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-id']

   







class VerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')
    is_verified = models.BooleanField(default=False, verbose_name='تم التحقق')
    code = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)], verbose_name='رمز التحقق')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    expires_at = models.DateTimeField(default=get_expiration_time, verbose_name='تاريخ الانتهاء')

    def __str__(self):
        return f'{self.user.username} code:{self.code}'



class Management(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']


class Registration(models.Model):
    phonenumber = models.CharField(unique=True,
                                        validators=[RegexValidator(
                                        regex=r'^\d{5,15}$'
                                    )], verbose_name='رقم الهاتف')
    first_name = models.CharField(max_length=50, verbose_name='الاسم الأول')
    father_name = models.CharField(max_length=50, verbose_name='اسم الأب')
    grand_father = models.CharField(max_length=50, verbose_name='اسم الجد')
    last_name = models.CharField(max_length=50, verbose_name='اسم العائلة')
    id_number = models.IntegerField(verbose_name='رقم الهوية')
    birthday = models.DateField(verbose_name='تاريخ الميلاد')
    job_position = models.CharField(choices=Job_position, max_length=50, null=True, blank=True, verbose_name='المهنة')
    gender = models.CharField(choices=Gender, max_length=10, verbose_name='الجنس')
    options_trip = models.CharField(choices=Options_trip, max_length=20, verbose_name='خيارات الرحلة')
    marital_status = models.CharField(choices=Marital_status, max_length=10, verbose_name='الحالة الاجتماعية')
    address = models.CharField(choices=Address, max_length=15, verbose_name='العنوان')
    alhajj = models.CharField(choices=Type_alhajj, max_length=50, null=True, blank=True, verbose_name='نوع الحج')
    tradition_reference = models.CharField(verbose_name='المرجع التقليدي')
    count_hajjas = models.BigIntegerField(null=True, blank=True, verbose_name='عدد مرات الحج')
    last_year = models.CharField(null=True, blank=True, verbose_name='آخر سنة حج')
    means_journey = models.CharField(choices=Means_journey, max_length=50, verbose_name='وسيلة السفر')
    blood_type = models.CharField(choices=Blood_type, null=True, blank=True, verbose_name='فصيلة الدم')
    illness = models.BooleanField(null=True, blank=True, verbose_name='مريض')
    tawaf = models.BooleanField(null=True, blank=True, verbose_name='طواف')
    sai = models.BooleanField(null=True, blank=True, verbose_name='سعي')
    wheelchair = models.BooleanField(null=True, blank=True, verbose_name='كرسي متحرك')
    type_help = models.CharField(max_length=500, null=True, blank=True, verbose_name='نوع المساعدة')




class Pilgrim(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')
    phonenumber = models.CharField(unique=True,
                                    db_index=True,
                                            validators=[RegexValidator(
                                            regex=r'^\d{5,15}$'
                                        )], verbose_name='رقم الهاتف')
    longitude = models.FloatField(max_length=100, default=24.3, verbose_name='خط الطول')
    latitude = models.FloatField(max_length=100, default=45.2, verbose_name='خط العرض')
    registeration_id = models.CharField(max_length=50, verbose_name='رقم التسجيل')
    first_name = models.CharField(max_length=50, verbose_name='الاسم الأول')
    father_name = models.CharField(max_length=50, verbose_name='اسم الأب')
    grand_father = models.CharField(max_length=50, verbose_name='اسم الجد')
    last_name = models.CharField(max_length=50, verbose_name='اسم العائلة')
    birthday = models.DateField(null=True, blank=True, verbose_name='تاريخ الميلاد')
    flight_num = models.IntegerField(null=True, blank=True, verbose_name='رقم الرحلة')
    flight_date = models.DateField(null=True, blank=True, verbose_name='تاريخ الرحلة')
    arrival = models.TimeField(null=True, blank=True, verbose_name='وقت الوصول')
    departure = models.TimeField(null=True, blank=True, verbose_name='وقت المغادرة')
    from_city = models.CharField(max_length=40, null=True, blank=True, verbose_name='من مدينة')
    to_city = models.CharField(max_length=40, null=True, blank=True, verbose_name='إلى مدينة')
    duration = models.CharField(max_length=40, null=True, blank=True, verbose_name='المدة')
    boarding_time = models.TimeField(null=True, blank=True, verbose_name='وقت الصعود')
    gate_num = models.IntegerField(null=True, blank=True, verbose_name='رقم البوابة')
    flight_company = models.CharField(max_length=50, verbose_name='شركة الطيران')
    company_logo = models.ImageField(null=True, blank=True, default='images/account.jpg', verbose_name='شعار الشركة')
    status = models.BooleanField(null=True, blank=True, verbose_name='الحالة')
    hotel = models.CharField(max_length=100, null=True, blank=True, verbose_name='الفندق')
    hotel_address = models.CharField(max_length=100, verbose_name='عنوان الفندق')
    room_num = models.IntegerField(null=True, blank=True, verbose_name='رقم الغرفة')
    haj_steps = models.ManyToManyField('HajSteps', blank=True, through='HaJStepsPilgrim', verbose_name='خطوات الحج')
    guide = models.ForeignKey('Guide', null=True, blank=True, on_delete=models.SET_NULL, verbose_name='المرشد')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')


    def __str__(self) -> str:
        return f'{self.user.username}'

    @property
    def last_step(self):
        return self.haj_steps.all().last()

    @property
    def guide_chat(self):
        try:
            guide_chat = Chat.objects.get(user=self.user, chat_type='guide')
            return guide_chat.id
        except Chat.DoesNotExist:
            return None 

    @property
    def manager_chat(self):
        try:
            guide_chat = Chat.objects.get(user=self.user, chat_type='guide')
            return guide_chat.id
        except Chat.DoesNotExist:
            return None 





class Guide(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, default=1, verbose_name='المستخدم')
    
    def __str__(self) -> str:
        return self.user.username



class Employee(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']




class Task(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='الموظف')
    title = models.CharField(max_length=500, unique=True, verbose_name='العنوان')
    content = models.CharField(max_length=100, verbose_name='المحتوى')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    completed = models.BooleanField(default=False, verbose_name='مكتمل')
    accepted = models.BooleanField(default=False, verbose_name='مقبول')

    def __str__(self) -> str:
        return f'{self.employee.user.username} : {self.title}'



class UserNotification(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')
    title = models.CharField(max_length=50, verbose_name='العنوان')
    content = models.CharField(max_length=200, verbose_name='المحتوى')
    info = models.CharField(max_length=200, null=True, blank=True, verbose_name='معلومات')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    def __str__(self) -> str:
        return f'{self.user.username} : {self.content}'
    


class BaseNotification(models.Model):
    sentBy = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='مرسل من')
    title = models.CharField(max_length=100, verbose_name='العنوان')
    content = models.CharField(max_length=200, verbose_name='المحتوى')
    info = models.CharField(max_length=200, verbose_name='معلومات')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    def __str__(self) -> str:
        return self.title




class Note(models.Model):
    pilgrim = models.ForeignKey(Pilgrim, on_delete=models.CASCADE, verbose_name='الحاج')
    guide = models.ForeignKey(Guide, on_delete=models.CASCADE, verbose_name='المرشد')
    content = models.CharField(max_length=500, null=True, blank=True, verbose_name='الملاحظات')
    audio = models.FileField(upload_to='audio/pilgrims', null=True, blank=True, verbose_name='الملف الصوتي')
    created = models.DateTimeField(auto_now_add=True, verbose_name='التاريخ')

    def __str__(self) -> str:
        return f'{self.pilgrim.user.username} : note'






class Chat(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='المستخدم')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    chat_type = models.CharField(choices=CHAT_CHOICES, max_length=20, default='guide', verbose_name='نوع المحادثة')

    objects = models.Manager()
    guide_chats = GuideChats()
    manager_chats = ManagerChats()

    def __str__(self) -> str:
        return f'{self.user.username} chat'




class AudioAttach(models.Model):
    file = models.FileField(upload_to='audio/chats', verbose_name='الملف') # to send audio record in chat




class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True, verbose_name='المرسل')
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, verbose_name='المحادثة')
    content = models.CharField(max_length=500, null=True, verbose_name='المحتوى')
    audio = models.ForeignKey(AudioAttach, on_delete=models.CASCADE, null=True, blank=True, verbose_name='الصوت')
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name='الوقت')
    seen = models.BooleanField(default=False, verbose_name='مشاهدة') # to see if the user read the message or not
    sent_user = models.BooleanField(default=False, verbose_name='تم الإرسال')

    def __str__(self):
        return f'{self.sender} : "{self.content[0:20]}..."'

    class Meta:
        ordering=['-timestamp']


class GuidanceCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاريخ الإنشاء')


    def __str__(self) -> str:
        return self.name



class GuidancePost(models.Model):
    category = models.ForeignKey(GuidanceCategory, on_delete=models.CASCADE, verbose_name='الفئة')
    title = models.CharField(max_length=100, verbose_name='العنوان')
    content = models.TextField(verbose_name='المحتوى')
    cover = models.ImageField(upload_to='cover', verbose_name='الغلاف')
    rank = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(1000)], verbose_name='الترتيب')
    created = models.DateField(auto_now_add=True, verbose_name='تاريخ الإنشاء') # datetime ?

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['rank']



class ReligiousCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')

    def __str__(self) -> str:
        return self.name



class ReligiousPost(models.Model):
    category = models.ForeignKey(ReligiousCategory, on_delete=models.CASCADE, verbose_name='الفئة')
    title = models.CharField(max_length=100, verbose_name='العنوان')
    content = models.TextField(verbose_name='المحتوى')
    cover = models.ImageField(upload_to='cover', verbose_name='الغلاف')
    rank = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(1000)], verbose_name='الترتيب')
    created = models.DateField(auto_now_add=True, verbose_name='تاريخ الإنشاء') # datetime ?

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['rank']



class SecondarySteps(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاريخ الإنشاء')
    note = models.CharField(max_length=500, default='note', verbose_name='ملاحظة')

    def __str__(self) -> str:
        return self.name
    




class HajSteps(models.Model):
    name = models.CharField(max_length=50, verbose_name='الاسم')
    rank = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1),MaxValueValidator(1000)], verbose_name='الترتيب')
    secondary_steps = models.ManyToManyField(SecondarySteps, verbose_name='الخطوات الثانوية')
    note = models.CharField(max_length=500, default='note', verbose_name='ملاحظة')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['rank']





class FormSubmission(models.Model):
    ip_address = models.CharField(max_length=45)
    submitted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-submitted_at']



class HaJStepsPilgrim(models.Model):
    pilgrim = models.ForeignKey(Pilgrim, on_delete=models.CASCADE, verbose_name='الحاج')
    haj_step = models.ForeignKey(HajSteps, on_delete=models.CASCADE, verbose_name='خطوة الحج')
    completed = models.BooleanField(default=False, verbose_name='مكتمل')

    def __str__(self):
        return f"{self.pilgrim.user.username}: {self.haj_step.name}"






class UserPassword(models.Model):
    username = models.CharField(max_length=100, verbose_name='اسم المستخدم')
    phonenumber = models.CharField(max_length=100, verbose_name='رقم الهاتف')
    password = models.CharField(max_length=100, verbose_name='كلمة المرور')

