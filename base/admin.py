from django.contrib import admin
from .models import *
from .resources import *
from import_export.admin import ImportExportModelAdmin
from fcm_django.models import FCMDevice
from fcm_django.admin import DeviceAdmin as DefaultDeviceAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin as DefaultOutstandingTokenAdmin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .utils.forms import *


admin.site.unregister(Group)

class HiddenModelAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        return {}





class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['id','user_type','username','first_name','last_name','phonenumber','is_verified','get_notifications']

    fieldsets = (
        (None, 
                {'fields':('phonenumber','email', 'password',)}
            ),
            ('User Information',
                {'fields':('username', 'first_name', 'last_name','image','user_type')}
            ),
            ('Permissions', 
                {'fields':('is_verified', 'get_notifications' ,'is_staff', 'is_superuser', 'is_active', 'groups','user_permissions',)}
            ),
            ('Registration', 
                {'fields':('date_joined', 'last_login',)}
            )
    )

    add_fieldsets = (
        (None, {'classes':('wide',),
            'fields':(
                'email', 'username','phonenumber', 'password1', 'password2'
            ),}
            ),
    )


class RegistrationAdmin(ImportExportModelAdmin):
    resource_class = RegistrationResource
    list_display = ['id','first_name','last_name','phonenumber']

    actions = ['restore']

    def restore(self, request, queryset):
        for form in queryset:
            form.is_deleted = False
            form.save()
        
    restore.short_description = "Restore selected forms"


class AudioAttachmentAdmin(ImportExportModelAdmin):
    resource_class = RegistrationResource
    list_display = ['id','file']



# class UserTypeAdmin(admin.ModelAdmin):
#     list_display = ['name']


class PilgrimAdmin(ImportExportModelAdmin):
    resource_class = PilgrimResource
    list_display = ['id','first_name','father_name','last_name','guide','phonenumber','flight_num','flight_company','arrival','departure','hotel','hotel_address','room_num','longitude','latitude']
    
    actions = ['restore']
    
    def restore(self, request, queryset):
        for pilgrim in queryset:
            user = pilgrim.user
            user.is_deleted = False
            user.save()
        
    restore.short_description = "Restore selected pilgrims"


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','username','phonenumber' , 'email']

    def email(self, obj):
        return obj.user.email

    def phonenumber(self, obj):
        return obj.user.phonenumber

    def username(self, obj):
        return obj.user.username

    def email(self, obj):
        return obj.user.email
    

class GuideAdmin(admin.ModelAdmin):
    list_display = ['id','username','phonenumber', 'email']

    def phonenumber(self, obj):
        return obj.user.phonenumber

    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username


class ManagementAdmin(admin.ModelAdmin):
    list_display = ['id','username','phonenumber' , 'email']

    def phonenumber(self, obj):
        return obj.user.phonenumber

    def email(self, obj):
        return obj.user.email

    def username(self, obj):
        return obj.user.username


class UserNotificationAdmin(admin.ModelAdmin):
    list_display = ['user','title','content','created']

class BaseNotificationAdmin(admin.ModelAdmin):
    list_display = ['sentBy','title','content','created']

class NoteAdmin(admin.ModelAdmin):
    list_display = ['id','pilgrim','guide','content','created']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','employee','title','content','created','completed','accepted']


class ChatAdmin(admin.ModelAdmin):
    list_display = ['id','user','created','chat_type','created']


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id','sender','chat','content','timestamp','sent_user']


class GuidanceCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class LiveStreamCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']


class GuidancePostAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','content','created']


class LiveStreamAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','content','created']


class ReligiousCategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','created']


class ReligiousPostAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','content','created']


class SecondaryStepsAdmin(admin.ModelAdmin):
    list_display = ['name']


class HajStepsAdmin(admin.ModelAdmin):
    list_display = ['name','display_secondary_steps']

    def display_secondary_steps(self, obj):
        return ', '.join([step.name for step in obj.secondary_steps.all()])
    display_secondary_steps.short_description = 'الخطوات الفرعية'



admin.site.register(Note,NoteAdmin)
admin.site.register(UserNotification,UserNotificationAdmin)
admin.site.register(BaseNotification,BaseNotificationAdmin)
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
admin.site.register(LiveStream,LiveStreamAdmin)
admin.site.register(ReligiousPost,ReligiousPostAdmin)
admin.site.register(ReligiousCategory,ReligiousCategoryAdmin)
admin.site.register(GuidanceCategory,GuidanceCategoryAdmin)
admin.site.register(LiveStreamCategory,LiveStreamCategoryAdmin)
admin.site.register(HajSteps,HajStepsAdmin)
admin.site.register(HaJStepsPilgrim)
admin.site.register(SecondarySteps,SecondaryStepsAdmin)
admin.site.register(VerificationCode)
admin.site.register(AudioAttach,AudioAttachmentAdmin)
admin.site.register(FormSubmission)