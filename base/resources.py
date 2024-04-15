from import_export import resources
from .models import *
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget


# class PilgrimResource(resources.ModelResource):
#     class Meta:
#         model = Pilgrim
#         exclude = ('id',)
#         fields = '__all__'

    # def get_import_id_fields(self):
    #     return ['name']


class PilgrimResource(resources.ModelResource):
    user = Field(
        column_name='مستخدم',
        attribute='user',
        widget=ForeignKeyWidget(model=CustomUser, field='id')
    )
    class Meta:
        model = Pilgrim

    def after_save_instance(self, instance, using_transactions, dry_run):
        if not dry_run:
            user_id = instance.user
            user = CustomUser.objects.get(id =user_id.id)
            user.set_password('oneoneone')
            Chat.objects.create(user=user)
            print("123")
            user.save()
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
    )
    chronic_diseases = Field(
        column_name='هل لديك أمراض مزمنة',
        attribute='chronic_diseases',
    )
    tawaf = Field(
        column_name='هل تحتاج لمن يساعدك خلال الطواف',
        attribute='tawaf',
    )
    sai = Field(
        column_name='هل تحتاج لمن يساعدك خلال السعي',
        attribute='sai',
    )
    wheelchair = Field(
        column_name='هل تحتاج إلى كرسي متحرك',
        attribute='wheelchair',
    )
    type_help = Field(
        column_name='يمكنك كتابة المساعدة المطلوبة',
        attribute='type_help',
    )
    class Meta:
        model = Registration
        exclude = ('id',)

    # def after_save_instance(self, instance, using_transactions, dry_run):
    #     if not dry_run:
    #         user_id = instance.user
    #         user = CustomUser.objects.get(id =user_id.id)
    #         user.set_password('oneoneone')
    #         Chat.objects.create(user=user)
    #         print("123")
    #         user.save()
    #     return True