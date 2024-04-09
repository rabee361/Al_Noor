from import_export import resources
from .models import *
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget

class PilgrimResource(resources.ModelResource):
    user = Field(
        column_name='user',
        attribute='user',
        widget=ForeignKeyWidget(model=CustomUser, field='id')
    )
    class Meta:
        model = Pilgrim
        # fields = ['id','user','flight_num','flight_date','gate_num','status','hotel','room_num','first_name', 'last_name', 'father_name', 
        #         'family_name',
        #         'identification_number', 'birthday','phonenumber', 'job_position','gender',
        #         'options_trip','marital_status','address','type_alhajj','tradition_reference','count_hajjas','last_year',
        #         'means_journey','blood_type','are_sick','chronic_diseases','tawaf','sai','wheelchair','type_help'
        #         ]
    def after_save_instance(self, instance, using_transactions, dry_run):
        user_id = instance.user
        user = CustomUser.objects.get(id =user_id.id)
        user.set_password('oneoneone')
        user.save()
        for i in range(2):
            chat_one = Chat.objects.get_or_create(user=user_id, type_chat='مرشد')
            chat_two = Chat.objects.get_or_create(user=user_id, type_chat='إدارة')
        return True