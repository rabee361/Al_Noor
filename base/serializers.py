from rest_framework import serializers
from .models import * 
from .utils import *
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



class ResetPasswordSerializer(serializers.Serializer):
    newpassword = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        password = attrs.get('password', '')
        newpassword = attrs.get('newpassword', '')
        validate_password(password)
        validate_password(newpassword)
        if password != newpassword:
            raise serializers.ValidationError({'message_error':'كلمات المرور لم تتطابق'})
        
        return attrs

    def save(self, **kwargs):
        user_id = self.context.get('user_id')
        user = CustomUser.objects.get(id=user_id)
        password = self.validated_data['newpassword']
        user.set_password(password)
        user.is_verified=False
        user.save()
        return user




class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'



class EmployeeSerializer(serializers.ModelSerializer):
    phonenumber = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Employee
        fields = '__all__'

    def get_phonenumber(self,obj):
        return obj.user.phonenumber.as_international
        



class CreateEmployeeSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    phonenumber = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):#### needs modification
        password = validated_data.get('password')
        phonenumber = validated_data.get('phonenumber')
        email = validated_data.get('email')
        username = validated_data.get('username')
        user = CustomUser.objects.create(username=username,email=email,phonenumber=phonenumber)
        user.set_password(password)
        user.save()
        validated_data['user'] = user
        employee = Employee.objects.create(user=user)
        return employee





class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'




class PilgrimSerializer(serializers.ModelSerializer):
    phonenumber = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Pilgrim
        fields = '__all__'

    def get_phonenumber(self,obj):
        return obj.phonenumber.as_international
        



class CreatePilgrimSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    phonenumber = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        password = validated_data.pop('password')
        phonenumber = validated_data.pop('phonenumber')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        father_name = validated_data.get('father_name')
        grand_father = validated_data.get('grand_father')
        full_name = first_name+father_name+grand_father+last_name
        user = CustomUser.objects.create(username=full_name,first_name=first_name,last_name=last_name,phonenumber=phonenumber)
        user.set_password(password)
        user.save()
        validated_data['user'] = user
        pilgrim = Pilgrim.objects.create(**validated_data)
        return pilgrim
    



class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = '__all__'



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
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



class ChatSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    username = serializers.CharField(source='user.username',read_only=True)

    class Meta:
        model = Chat
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.user.image:
            return request.build_absolute_uri(obj.user.image.url)
        return None


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'


class GuidancePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidancePost
        fields = '__all__'


class ReligiousPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReligiousPost
        fields = '__all__'


class GuidanceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GuidanceCategory
        fields = '__all__'
        

class ReligiousCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ReligiousCategory
        fields = '__all__'



class SecondaryStepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondarySteps
        fields = ['name','note']




class HajStepSerializer(serializers.ModelSerializer):
    secondary_steps = SecondaryStepsSerializer(many=True)

    class Meta:
        model = HajSteps
        fields = '__all__'
