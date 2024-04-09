from import_export import resources
from .models import *
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget
import tablib
import os


class PilgrimResource(resources.ModelResource):
    user = Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(model=CustomUser, field='id')
    )
    class Meta:
        model = Pilgrim
        fields = ['id','user','flight_num','flight_date','gate_num','status','hotel','room_num','first_name', 'last_name', 'father_name', 
                'family_name',
                'identification_number', 'birthday','phonenumber', 'job_position','gender',
                'options_trip','marital_status','address','type_alhajj','tradition_reference','count_hajjas','last_year',
                'means_journey','blood_type','are_sick','chronic_diseases','tawaf','sai','wheelchair','type_help'
                ]
    def after_save_instance(self, instance, using_transactions, dry_run):
        user_id = instance.user
        user = CustomUser.objects.get(id =user_id.id)
        user.set_password('oneoneone')
        user.save()
        print(user)
        print(f'Instance {instance.id} has been saved')