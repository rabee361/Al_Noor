from django.contrib import admin
from .models import *
from .resources import *
from import_export.admin import ImportExportModelAdmin



class PilgrimAdmin(ImportExportModelAdmin): 
    resource_class = PilgrimResource
    list_display = ['id', 'flight_num']


admin.site.register(Note)
admin.site.register(UserNotification)
admin.site.register(CustomUser)
admin.site.register(Pilgrim,PilgrimAdmin)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Guide)
admin.site.register(Chat)
admin.site.register(ChatMessage)
admin.site.register(VerificationCode)