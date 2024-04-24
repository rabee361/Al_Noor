from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from .utils import *
from .options import *
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='images/users',default='images/account.jpg' , verbose_name="الصورة الشخصية")
    phonenumber = PhoneNumberField(region='SA',unique=True , verbose_name="رقم الهاتف")
    is_verified = models.BooleanField(default=False , verbose_name="تم التوثيق")
    get_notifications = models.BooleanField(default=True , verbose_name="تلقي اشعارات")
    username = models.CharField(max_length=255, blank=True, null=True , verbose_name="الاسم الكامل")

    USERNAME_FIELD = 'phonenumber'
    REQUIRED_FIELDS = ('username',)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ['-id']
        verbose_name = ("مستخدم")
        verbose_name_plural = ("مستخدمين")
   



class VerificationCode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    code = models.IntegerField(validators=[MinValueValidator(1000), MaxValueValidator(9999)])
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField(default=get_expiration_time)

    def __str__(self):
        return f'{self.user.username} code:{self.code}'

    class Meta:
        verbose_name = ("رمز التأكيد")
        verbose_name_plural = ("رموز التأكيد")


# # in case we needed to store the hotel info in a seperate model
# # class Hotel():
# #     pass



class Management(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']
        verbose_name = ("مدير")
        verbose_name_plural = ("الادارة")


class Registration(models.Model):
    phonenumber = PhoneNumberField(region='SA',unique=True , verbose_name="رقم الهاتف")
    first_name = models.CharField(max_length=50 , verbose_name="الاسم الأول")
    father_name = models.CharField(max_length=50 , verbose_name="اسم الأب")
    grand_father = models.CharField(max_length=50 , verbose_name="اسم الجد")
    last_name = models.CharField(max_length=50 , verbose_name="العائلة")
    id_number = models.IntegerField(verbose_name="رقم الهوية")
    birthday = models.DateField(verbose_name="الميلاد")
    job_position = models.CharField(choices=Job_position, max_length=50, null=True, blank=True, verbose_name="الوظيفة")
    gender = models.CharField(choices=Gender, max_length=10, verbose_name="الجنس")
    options_trip = models.CharField(choices=Options_trip, max_length=20, verbose_name="خيارات الرحلة")
    marital_status = models.CharField(choices=Marital_status, max_length=10, verbose_name="الحالة الاجتماعية")
    address = models.CharField(choices=Address, max_length=15, verbose_name="مكان السكن")
    alhajj = models.CharField(choices=Type_alhajj, max_length=50, null=True, blank=True, verbose_name="نوع الحجة")
    tradition_reference = models.CharField(choices=Tradition_reference, verbose_name="مرجع التقليد")
    count_hajjas = models.BigIntegerField(null=True, blank=True, verbose_name="عدد الحجات")
    last_year = models.CharField(null=True, blank=True, verbose_name="اخر سنة حج")
    means_journey = models.CharField(choices=Means_journey, max_length=50, verbose_name="وسيلة الرحلة")
    blood_type = models.CharField(choices=Blood_type, null=True, blank=True, verbose_name="فصيلة الدم")
    illness = models.BooleanField(null=True, blank=True, verbose_name="أمراض")
    chronic_diseases = models.CharField(null=True, blank=True, max_length=200, verbose_name="أمراض مزمنة")
    tawaf = models.BooleanField(null=True, blank=True, verbose_name="مساعدة في الطواف")
    sai = models.BooleanField(null=True, blank=True, verbose_name="مساعدة في السعي")
    wheelchair = models.BooleanField(null=True, blank=True, verbose_name="كرسي متحرك")
    type_help = models.TextField(null=True, blank=True, verbose_name="نوع المساعدة")

    class Meta:
        verbose_name = ("استمارة تسجيل")
        verbose_name_plural = ("استمارات التسجيل")



class Pilgrim(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE , verbose_name="المستخدم")
    registeration_id = models.CharField(max_length=50 , verbose_name="رقم الهوية")
    first_name = models.CharField(max_length=50 , verbose_name="الاسم الأول")
    father_name = models.CharField(max_length=50 , verbose_name="اسم الأب")
    grand_father = models.CharField(max_length=50 , verbose_name="اسم الجد")
    last_name = models.CharField(max_length=50 , verbose_name="العائلة")
    birthday = models.DateField(verbose_name="الميلاد")
    phonenumber = PhoneNumberField(region='SA',unique=True , verbose_name="رقم الهاتف")
    flight_num = models.IntegerField(null=True, blank=True,verbose_name="رقم الرحلة")
    arrival = models.DateTimeField(verbose_name="موعد الوصول")
    departure = models.DateTimeField(verbose_name="موعد الاقلاع")
    duration = models.DurationField(verbose_name="مدة الرحلة")
    borading_time = models.TimeField(verbose_name="وقت الصعود")####
    gate_num = models.IntegerField(null=True, blank=True , verbose_name="رقم البوابة")####
    flight_company = models.CharField(max_length=50 , verbose_name="رقم الرحلة") ### can be a choice list
    company_logo = models.ImageField(verbose_name="شعار الشركة") ###
    status = models.BooleanField(null=True, blank=True , verbose_name="الحالة")
    hotel = models.CharField(max_length=100, null=True, blank=True , verbose_name="الفندق")
    hotel_address = models.CharField(max_length=100 , verbose_name="عنوان الفندق") #### link to google maps can be long and lat
    room_num = models.IntegerField(null=True, blank=True , verbose_name="رقم الغرفة")
    haj_steps = models.ManyToManyField('HajSteps' , blank=True)


    def __str__(self) -> str:
        return f'{self.id} - {self.id}'

    class Meta:
        verbose_name = ("حاج")
        verbose_name_plural = ("الحجاج")


class Guide(models.Model):
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE ,default=1)
    
    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = ("المرشد")
        verbose_name_plural = ("المرشدين")


class Employee(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
    class Meta:
        ordering = ['-id']
        verbose_name = ("موظف")
        verbose_name_plural = ("موظفين")



class Task(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,verbose_name="الموظف")
    title = models.CharField(max_length=500,unique=True, verbose_name="اسم المهمة")
    content = models.CharField(max_length=100, verbose_name="المحتوى")
    created = models.DateTimeField(auto_now_add=True, verbose_name="التاريخ")
    completed = models.BooleanField(default=False, verbose_name="اكتملت")
    accepted = models.BooleanField(default=False, verbose_name="تم قبولها")

    def __str__(self) -> str:
        return f'{self.employee.user.username} : {self.title}'

    class Meta:
        verbose_name = ("مهمة")
        verbose_name_plural = ("مهام")



class UserNotification(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE , verbose_name="المستخدم")
    title = models.CharField(max_length=50 , verbose_name="العنوان")
    content = models.CharField(max_length=200 , verbose_name="المحتوى")
    info = models.CharField(max_length=200 , null=True , blank=True , verbose_name="معلومات اضافية")
    created = models.DateTimeField(auto_now_add=True , verbose_name="التاريخ")

    def __str__(self) -> str:
        return f'{self.user.username} : {self.content}'
    
    class Meta:
        verbose_name = ("اشعار")
        verbose_name_plural = ("اشعارات")



class Note(models.Model):
    pilgrim = models.ForeignKey(Pilgrim,on_delete=models.CASCADE , verbose_name="الحاج")
    guide = models.ForeignKey(Guide,on_delete=models.CASCADE , verbose_name="المرشد")
    content = models.CharField(max_length=500 , verbose_name="المحتوى")
    created = models.DateTimeField(auto_now_add=True , verbose_name="التاريخ")

    def __str__(self) -> str:
        return f'{self.pilgrim.user.username} : {self.content}'

    class Meta:
        verbose_name = ("ملاحظة")
        verbose_name_plural = ("ملاحظات")



class Chat(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE , verbose_name="المستخدم")
    created = models.DateTimeField(auto_now_add=True , verbose_name="تاريخ الانشاء")

    def __str__(self) -> str:
        return f'{self.user.username} chat'

    class Meta:
        verbose_name = ("محادثة")
        verbose_name_plural = ("محادثات")



class ChatMessage(models.Model):
    sender = models.ForeignKey(CustomUser , on_delete=models.CASCADE , verbose_name="المرسل")
    chat = models.ForeignKey(Chat , on_delete=models.CASCADE , verbose_name="المحادثة")
    content = models.CharField(max_length=500 , verbose_name="المحتوى")
    timestamp = models.DateTimeField(auto_now_add=True , verbose_name="التاريخ والوقت")
    employee = models.BooleanField(default=False , verbose_name="الموظف")

    def __str__(self):
        return f'{self.sender} : "{self.content[0:20]}..."'

    class Meta:
        ordering=['-timestamp']
        verbose_name = ("رسالة")
        verbose_name_plural = ("رسائل")



class GuidanceCategory(models.Model):
    name = models.CharField(max_length=50 , verbose_name="اسم الفئة")
    created = models.DateTimeField(auto_now_add=True,null=True , verbose_name="تاريخ الانشاء")


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ("نوع الارشاد")
        verbose_name_plural = ("أنواع الارشاد الديني")




class GuidancePost(models.Model):
    category = models.ForeignKey(GuidanceCategory, on_delete=models.CASCADE, verbose_name="الفئة")
    title = models.CharField(max_length=100, verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    cover = models.ImageField(upload_to='cover', verbose_name="صورة الغلاف")
    created = models.DateField(auto_now_add=True, verbose_name="تاريخ الانشاء") ##datetime ??

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-created']
        verbose_name = ("إرشاد ديني")
        verbose_name_plural = ("إرشادات دينية")



class ReligiousCategory(models.Model):
    name = models.CharField(max_length=50 , verbose_name="اسم الفئة")
    created = models.DateTimeField(auto_now_add=True , verbose_name="تاريخ الانشاء")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = ("نوع عمل ديني")
        verbose_name_plural = ("أنواع العمل الديني")



class ReligiousPost(models.Model):
    category = models.ForeignKey(ReligiousCategory, on_delete=models.CASCADE , verbose_name="الفئة")
    title = models.CharField(max_length=100 , verbose_name="العنوان")
    content = models.TextField(verbose_name="المحتوى")
    cover = models.ImageField(upload_to='cover' , verbose_name="صورة الغلاف")
    created = models.DateField(auto_now_add=True , verbose_name="تاريخ الانشاء")## datetime ?

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-created']
        verbose_name = ("عمل ديني")
        verbose_name_plural = ("أعمال دينية")




class SecondarySteps(models.Model):
    name = models.CharField(max_length=50,verbose_name="الاسم")
    note = models.CharField(max_length=500,default='note',verbose_name="ملاحظة")
    created = models.DateTimeField(auto_now_add=True,verbose_name="تاريخ الانشاء")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = ("خطوة فرعية")
        verbose_name_plural = ("خطوات فرعية")




class HajSteps(models.Model):
    name = models.CharField(max_length=50 , verbose_name="الخطوة")
    secondary_steps = models.ManyToManyField(SecondarySteps , verbose_name="خطوات فرعية")
    

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = ("خطوة")
        verbose_name_plural = ("خطوات الأعمال الديني")
