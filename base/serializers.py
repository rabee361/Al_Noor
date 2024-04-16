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

class UpdateImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('image',)

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
    username = serializers.CharField(write_only=True)
    phonenumber = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Employee
        fields = '__all__'
    
    def create(self, validated_data):
        username = validated_data.pop('username')
        phonenumber = validated_data.pop('phonenumber')
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        user = CustomUser.objects.create(phonenumber=phonenumber, username=username, email=email)
        user.set_password(password)
        user.save()
        instance = Employee.objects.create(user=user)
        return instance



class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'


class AhkamAlmrahSerialzier(serializers.ModelSerializer):
    class Meta:
        model = AhkamAlmrah
        fields = '__all__'

class TypeAhkamAlmrahSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeAhkamAlmrah
        fields = '__all__'

class PilgrimSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Pilgrim
        fields = '__all__'

    def create(self, validated_data):
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')
        phonenumber = validated_data.pop('phonenumber')
        password = generate_password()
        user = CustomUser.objects.create(phonenumber=phonenumber, username=f'{first_name} {last_name}')
        user.set_password(password)
        user.save()
        instance = Pilgrim.objects.create(user=user, first_name=first_name, last_name=last_name,phonenumber=phonenumber, **validated_data)
        return instance


# class InfoFlowSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Pilgrim
#         fields = ['flight_num', 'arrival', 'departure', 'duration', 'borading_time', 'gate_num', 'flight_company', 'company_logo', 'status']


# class InfoHotelSerializer(serializers.ModelSerializer):
#     class Meta:
#         fields = ['hotel', 'hotel_address', 'room_num']

        
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
