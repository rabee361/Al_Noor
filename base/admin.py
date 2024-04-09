from django.contrib import admin
from import_export.admin import ImportExportMixin, ExportMixin
from .resources import *

class PilgirmAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_classes = [PilgrimResource,]

admin.site.register(Pilgrim, PilgirmAdmin)

admin.site.register(CustomUser)

admin.site.register(Chat)

admin.site.register(TypeGuidance)
admin.site.register(ReligiousGuide)

admin.site.register(TypeReligious)
admin.site.register(ReligiousWorks)