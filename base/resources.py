from import_export import resources
from .models import *
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget  , BooleanWidget
from .utils.utils import generate_password



class YesNoBooleanWidget(BooleanWidget):
    def render(self, value, obj=None):
        if value:
            return 'نعم'
        return 'لا'


class PilgrimResource(resources.ModelResource):
    first_name = Field(
        column_name='الاسم الأول',
        attribute='first_name',
    )
    father_name = Field(
        column_name='اسم الأب',
        attribute='father_name',
    )
    grand_father = Field(
        column_name='اسم الجد',
        attribute='grand_father',
    )
    last_name = Field(
        column_name='العائلة',
        attribute='last_name',
    )
    email = Field(
        column_name='الايميل',
        attribute='email',
    )
    birthday = Field(
        column_name='تاريخ الميلاد - الميلادي فقط',
        attribute='birthday',
    )
    phonenumber = Field(
        column_name='رقم الجوال',
        attribute='phonenumber',
    )
    flight_num = Field(
        column_name='رقم الرحلة',
        attribute='flight_num',
    )
    flight_date = Field(
        column_name='تاريخ الرحلة',
        attribute='flight_date',
    )
    registeration_id = Field(
        column_name='رقم الهوية',
        attribute='registeration_id',
    )
    from_city = Field(
        column_name='من المدينة',
        attribute='from_city',
    )
    to_city = Field(
        column_name='إلى المدينة',
        attribute='to_city',
    )
    arrival = Field(
        column_name='موعد الوصول',
        attribute='arrival',
    )
    departure = Field(
        column_name='موعد الرحيل',
        attribute='departure',
    )
    boarding_time = Field(
        column_name='وقت الصعود',
        attribute='boarding_time',
    )
    gate_num = Field(
        column_name='رقم البوابة',
        attribute='gate_num',
    )
    flight_company = Field(
        column_name='شركة الطيران',
        attribute='flight_company',
    )
    company_logo = Field(
        column_name='شعار الشركة',
        attribute='company_logo',
    )
    status = Field(
        column_name='الحالة',
        attribute='status',
    )
    hotel = Field(
        column_name='الفندق',
        attribute='hotel',
    )
    hotel_address = Field(
        column_name='عنوان الفندق',
        attribute='hotel_address',
    )
    room_num = Field(
        column_name='رقم الغرفة',
        attribute='room_num',
    )

    class Meta:
        model = Pilgrim
        exclude = ['user','id','created','duration','haj_steps','guide','longitude','latitude','company_logo']
        import_id_fields = ['phonenumber']

    def before_import_row(self, row, **kwargs):
        phonenumber = row['رقم الجوال']
        email = row['الايميل']
        first_name = row['الاسم الأول']
        last_name = row['العائلة']
        user, created = CustomUser.objects.get_or_create(phonenumber=phonenumber)
        if created:
            chat1 = Chat.objects.create(user=user , chat_type='guide')
            chat2 = Chat.objects.create(user=user , chat_type='manager')
        user.username = first_name
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.user_type = 'حاج'
        my_password = generate_password()
        user.set_password(my_password)
        user.save()

    def after_save_instance(self, instance, using_transactions, dry_run):
        if not dry_run:
            instance.user = CustomUser.objects.get(phonenumber=instance.phonenumber)
            instance.save()
        return True





class RegistrationResource(resources.ModelResource):
    phonenumber = Field(
        column_name='رقم الجوال',
        attribute='phonenumber',
    )
    first_name = Field(
        column_name='الاسم الأول',
        attribute='first_name',
    )
    father_name = Field(
        column_name='اسم الأب',
        attribute='father_name',
    )
    grand_father = Field(
        column_name='اسم الجد',
        attribute='grand_father',
    )
    last_name = Field(
        column_name='العائلة',
        attribute='last_name',
    )
    id_number = Field(
        column_name='رقم الهوية',
        attribute='id_number',
    )
    email = Field(
        column_name='الايميل',
        attribute='email',
    )
    birthday = Field(
        column_name='تاريخ الميلاد - الميلادي فقط',
        attribute='birthday',
    )
    job_position = Field(
        column_name='الوظيفة',
        attribute='job_position',
    )
    gender = Field(
        column_name='الجنس',
        attribute='gender',
    )
    options_trip = Field(
        column_name='خيارات الرحلة',
        attribute='options_trip',
    )
    marital_status = Field(
        column_name='الحالة الاجتماعية',
        attribute='marital_status',
    )
    address = Field(
        column_name='مكان السكن',
        attribute='address',
    )
    alhajj = Field(
        column_name='نوع الحجة',
        attribute='alhajj',
    )
    tradition_reference = Field(
        column_name='مرجع التقليد',
        attribute='tradition_reference',
    )
    count_hajjas = Field(
        column_name='عدد الحجات',
        attribute='count_hajjas',
    )
    last_year = Field(
        column_name='اخر سنة حججت فيها',
        attribute='last_year',
    )
    means_journey = Field(
        column_name='وسيلة الرحلة',
        attribute='means_journey',
    )
    blood_type = Field(
        column_name='فصيلة الدم',
        attribute='blood_type',
    )
    illness = Field(
        column_name='هل لديك أمراض مزمنة',
        attribute='illness',
        widget=YesNoBooleanWidget(),
    )
    chronic_diseases = Field(
        column_name='هل لديك أمراض مزمنة',
        attribute='chronic_diseases',
    )
    additional = Field(
        column_name="اسم المرافق معك",
        attribute='additional'
    )
    tawaf = Field(
        column_name='هل تحتاج لمن يساعدك خلال الطواف',
        attribute='tawaf',
        widget=YesNoBooleanWidget(),
    )
    sai = Field(
        column_name='هل تحتاج لمن يساعدك خلال السعي',
        attribute='sai',
        widget=YesNoBooleanWidget(),
    )
    wheelchair = Field(
        column_name='هل تحتاج إلى كرسي متحرك',
        attribute='wheelchair',
        widget=YesNoBooleanWidget(),
    )
    type_help = Field(
        column_name='يمكنك كتابة المساعدة المطلوبة',
        attribute='type_help',
    )
    class Meta:
        model = Registration
        exclude = ('id',)

