from rest_framework import serializers
from .models import * 
from .utils import weekday_mapping
from datetime import datetime






class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'



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
