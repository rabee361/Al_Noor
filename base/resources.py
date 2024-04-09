from import_export import resources
from .models import *
from import_export.fields import Field
from import_export.widgets import ForeignKeyWidget


# class PilgrimResource(resources.ModelResource):
#     class Meta:
#         model = Pilgrim
        # exclude = ('id',)
        
    # def get_import_id_fields(self):
    #     return ['name']


class PilgrimResource(resources.ModelResource):
    user = Field(
        column_name='user',
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