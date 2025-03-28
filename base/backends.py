from django.contrib.auth.backends import ModelBackend
from .models import CustomUser

class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, phonenumber=None, password=None, **kwargs):

        try:
            user = CustomUser.objects.get(phonenumber=phonenumber, is_deleted=False)
        except CustomUser.DoesNotExist:
            return None

        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id, is_deleted=False)
        except CustomUser.DoesNotExist:
            return None