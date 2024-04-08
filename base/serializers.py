from rest_framework import serializers
from .models import * 
from .utils import weekday_mapping
from datetime import datetime
from django.contrib.auth import  authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import TokenError, RefreshToken



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'), username=username, password=password)
            if not user:
                raise serializers.ValidationError("Incorrect Credentials")
            if not user.is_active:
                raise serializers.ValidationError({'message_error':'this account is not active'})
        else:
            raise serializers.ValidationError('Must include "username" and "password".')

        data['user'] = user
        return data
    


class LogoutUserSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs
    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')





class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'


class PilgrimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pilgrim
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'



class HijriSerializer(serializers.Serializer):
    day = serializers.CharField()
    month = serializers.CharField()
    year = serializers.CharField()
    weekday = serializers.CharField()


class GregorianSerializer(serializers.Serializer):
    day = serializers.CharField()
    month = serializers.CharField()
    year = serializers.CharField()
