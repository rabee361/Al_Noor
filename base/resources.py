from import_export import resources
from .models import *


class PilgrimResource(resources.ModelResource):
    class Meta:
        model = Pilgrim
        # exclude = ('id',)
        
    # def get_import_id_fields(self):
    #     return ['name']