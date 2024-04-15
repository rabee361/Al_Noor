from django.contrib import admin
from .models import *
from .resources import *
from import_export.admin import ImportExportModelAdmin


### needs modification
class PilgrimAdmin(ImportExportModelAdmin):
    resource_class = PilgrimResource
    list_display = ['id']

class RegistrationAdmin(ImportExportModelAdmin):
    resource_class = RegistrationResource
    list_display = ['id']


admin.site.register(Note)
admin.site.register(UserNotification)
admin.site.register(CustomUser)
admin.site.register(Pilgrim,PilgrimAdmin)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Employee)
admin.site.register(Management)
admin.site.register(Task)
admin.site.register(Guide)
admin.site.register(Chat)
admin.site.register(ChatMessage)
admin.site.register(VerificationCode)