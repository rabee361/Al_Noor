from django.contrib import admin
from .models import *
from .resources import *
from import_export.admin import ImportExportModelAdmin
from .forms import *



class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    list_display = ['id','first_name','last_name','phonenumber','is_verified','get_notifications']



class RegistrationAdmin(ImportExportModelAdmin):
    resource_class = RegistrationResource
    list_display = ['id']


### needs modification
class PilgrimAdmin(ImportExportModelAdmin):
    resource_class = PilgrimResource
    list_display = ['id','first_name','father_name','last_name','phonenumber','flight_num','flight_company','arrival','departure','hotel','hotel_address','room_num']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def phonenumber(self, obj):
        return obj.user.phonenumber



class GuideAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def phonenumber(self, obj):
        return obj.user.phonenumber



class ManagementAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','last_name']

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def phonenumber(self, obj):
        return obj.user.phonenumber


class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ['user','title','content','created']


class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','pilgrim','guide','content','created']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','employee','title','content','created','completed']


class ChatAdmin(admin.ModelAdmin):
    list_display = ['id','user','created']


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id','sender','chat','content','timestamp','employee']


class GuidanceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class GuidancePostAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','content','created']


class ReligiousCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','created']


class ReligiousPostAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','content','created']




admin.site.register(Note,NoteAdmin)
admin.site.register(UserNotification,UserNotificationAdmin)
admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Pilgrim,PilgrimAdmin)
admin.site.register(Registration,RegistrationAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Management,ManagementAdmin)
admin.site.register(Task,TaskAdmin)
admin.site.register(Guide,GuideAdmin)
admin.site.register(Chat,ChatAdmin)
admin.site.register(ChatMessage,ChatMessageAdmin)
admin.site.register(GuidancePost,GuidancePostAdmin)
admin.site.register(ReligiousPost,ReligiousPostAdmin)
admin.site.register(ReligiousCategory,ReligiousCategoryAdmin)
admin.site.register(GuidanceCategory,GuidanceCategoryAdmin)
admin.site.register(VerificationCode)

admin.site.register(TypeAhkamAlmrah)
admin.site.register(AhkamAlmrah)