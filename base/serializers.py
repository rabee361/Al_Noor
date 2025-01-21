from rest_framework import serializers
from .models import * 
from .utils.utils import *
from datetime import datetime
from django.contrib.auth import  authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import TokenError, RefreshToken
from rest_framework.exceptions import ValidationError
import re

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

        user = authenticate(request=self.context.get('request'), username=username, password=password)
        if not user:
            raise serializers.ValidationError({"error":"لا يوجد مستخدم بهذه المعلومات"})
        if not user.is_active:
            raise serializers.ValidationError({"error":"هذا الحساب غير مفعل"})

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






class HajStepsPilgrimSerializer(serializers.ModelSerializer):
    class Meta:
        model = HaJStepsPilgrim
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





class NoteSerializer(serializers.ModelSerializer):
    guide = serializers.CharField(required=False)

    class Meta:
        model = Note
        fields = '__all__'

    def validate(self, attrs):
        if not attrs.get('audio') and not attrs.get('content'):
            raise ValidationError("content and audio can't be empty together.")
        return attrs
            

    def create(self, validated_data):
        user = self.context['request'].user
        guide = Guide.objects.get(user=user)
        note = Note.objects.create(
            guide=guide,
            **validated_data
        )
        return note




class EmployeeSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    username = serializers.CharField(source='user.username')
    email = serializers.CharField(source='user.email')
    image = serializers.ImageField(source='user.image',read_only=True)
    phonenumber = serializers.CharField(source='user.phonenumber',read_only=True)
     
    class Meta:
        model = Employee
        fields = '__all__'

    def get_user(self,obj):
        return obj.user.id





class CreateEmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    phonenumber = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        exclude = ['user']
    def validate(self, attrs):
        email = attrs.get('email')
        phonenumber = attrs.get('phonenumber')
        if not re.match(r'^\d{5,15}$', phonenumber):
            raise serializers.ValidationError({"error": "رقم الهاتف يجب أن يكون من 5 إلى 15 رقم"})
        if CustomUser.objects.filter(phonenumber=phonenumber).exists():
            raise serializers.ValidationError({"error": "هذا الرقم موجود مسبقا"})
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError({"error": "هذا البريد الإلكتروني موجود مسبقا"})
        return super().validate(attrs)

    def create(self,validated_data):#### needs modification
        password = validated_data.get('password')
        phonenumber = validated_data.get('phonenumber')
        email = validated_data.get('email')
        username = validated_data.get('username')
        user = CustomUser.objects.create(username=username,email=email,phonenumber=phonenumber)
        user.set_password(password)
        user.user_type = 'موظف'
        user.save()
        validated_data['user'] = user
        employee = Employee.objects.create(user=user)
        return employee


class UpdateEmployeeSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    phonenumber = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    # password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        exclude = ['user']

    def update(self, instance, validated_data):
        username = validated_data.get('username')
        phonenumber = validated_data.get('phonenumber')
        email = validated_data.get('email')
        user = instance.user
        user.username = username
        user.email = email
        if user.phonenumber != phonenumber:
            if Employee.objects.filter(user__phonenumber=phonenumber).exists():
                raise serializers.ValidationError({"error": "هذا الرقم موجود مسبقا"})
            else:
                user.phonenumber = phonenumber
        try:
            password = validated_data.get('password')
            user.set_password(password)
        except:
            pass
        # user.phonenumber = phonenumber
        user.save()
        employee = Employee.objects.get(user=user)

        return employee




class ManagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Management
        fields = '__all__'






class GuideSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    image = serializers.ImageField(source='user.image' , read_only=True)
    email = serializers.CharField(source='user.email' , read_only=True)
    
    class Meta:
        model = Guide
        fields = ['id','username','image','email']





class SimpleGuideSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username',read_only=True)
    image = serializers.ImageField(source='user.image',read_only=True)

    class Meta:
        model = Guide
        fields = ['id','username','image']

 

class PilgrimSerializer(serializers.ModelSerializer):
    guide_chat = serializers.SerializerMethodField(read_only=True)
    guide_id = serializers.SerializerMethodField(read_only=True)
    manager_chat = serializers.SerializerMethodField(read_only=True)
    duration = serializers.SerializerMethodField()
    image = serializers.ImageField(source='user.image',read_only=True)
    active = serializers.BooleanField(source='user.is_active',read_only=True)
    guide = SimpleGuideSerializer(many=False)
    haj_steps = serializers.SerializerMethodField(read_only=True)
    last_step = serializers.SerializerMethodField(read_only=True)
    notes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pilgrim
        fields = '__all__'

    def get_notes(self,obj):
        pilgrim_notes = Note.objects.filter(pilgrim=obj)
        serializer = NoteSerializer(pilgrim_notes , many=True)
        return serializer.data

    def get_guide_id(self, obj):
        return obj.guide.user.id if obj.guide else 0


    def get_haj_steps(self, obj):
        haj_steps_data = []
        steps = HaJStepsPilgrim.objects.only('haj_step').filter(pilgrim=obj).values('haj_step')
        total_steps = HajSteps.objects.only('name').values('name')

        for haj_step_pilgrim in total_steps:
            if steps.filter(haj_step__name=haj_step_pilgrim['name']).exists():
                is_completed = True
            else:
                is_completed = False

            haj_steps_data.append({
                'haj_step': haj_step_pilgrim['name'],
                'completed': is_completed,
            })
        return haj_steps_data
    

    def get_last_step(self,obj):
        if obj.last_step:
            return obj.last_step.name
        else:
            return None

        
    def get_guide_chat(self, obj):
        try:
            guide_chat = Chat.objects.get(user=obj.user , chat_type='guide')
            return guide_chat.id
        except Chat.DoesNotExist:
            return None 
        
    def get_manager_chat(self, obj):
        try:
            manager_chat = Chat.objects.get(user=obj.user , chat_type='manager')
            return manager_chat.id
        except Chat.DoesNotExist:
            return None 
        
    def get_duration(self, obj):
        duration = obj.duration
        formatted_duration = str(duration).split('.')[0]  # Remove microseconds
        return formatted_duration        





class ListPilgrimSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()
    image = serializers.ImageField(source='user.image',read_only=True)
    active = serializers.BooleanField(source='user.is_active',read_only=True)
    notes = serializers.SerializerMethodField(read_only=True)
    manager_chat = serializers.SerializerMethodField(read_only=True)
    guide_chat = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Pilgrim
        exclude = ['guide','haj_steps']


    def get_notes(self,obj):
        pilgrim_notes = Note.objects.filter(pilgrim=obj)
        serializer = NoteSerializer(pilgrim_notes , many=True)
        return serializer.data
    

    def get_guide_chat(self, obj):
        return obj.guide_chat
        

    def get_manager_chat(self, obj):
        return obj.manager_chat
        

    def get_duration(self, obj):
        duration = obj.duration
        formatted_duration = str(duration).split('.')[0]  # Remove microseconds
        return formatted_duration        







class HajStepsPilgrimSerializer(serializers.ModelSerializer):
    haj_step = HajStepSerializer(many=False , read_only=True)

    class Meta:
        model = HaJStepsPilgrim
        fields = ['haj_step','completed']







class CreatePilgrimSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Pilgrim
        exclude = ['user','haj_steps']

    def validate(self, attrs):
        email = attrs.get('email')
        phonenumber = attrs.get('phonenumber')
        if not re.match(r'^\d{5,15}$', phonenumber):
            raise serializers.ValidationError({"error": "رقم الهاتف يجب أن يكون من 5 إلى 15 رقم"})
        if CustomUser.objects.filter(phonenumber=phonenumber).exists():
            raise serializers.ValidationError({"error": "هذا الرقم موجود مسبقا"})

    def create(self , validated_data):
        password = validated_data.pop('password')
        phonenumber = validated_data.get('phonenumber')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        father_name = validated_data.get('father_name')
        grand_father = validated_data.get('grand_father')
        arrival_datetime = datetime.strptime(str(validated_data.get('arrival')), '%H:%M:%S')
        departure_datetime = datetime.strptime(str(validated_data.get('departure')), '%H:%M:%S')
        validated_data['duration'] = arrival_datetime - departure_datetime
        full_name = first_name+father_name+grand_father+last_name
        user = CustomUser.objects.create(username=full_name,first_name=first_name,last_name=last_name,phonenumber=phonenumber)
        user.set_password(password)
        user.user_type = 'حاج'
        Chat.objects.create(user=user , chat_type='guide')
        Chat.objects.create(user=user , chat_type='manager')
        user.save()
        validated_data['user'] = user
        pilgrim = Pilgrim.objects.create(**validated_data)
        return pilgrim






class UpdatePilgrimSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pilgrim
        exclude = ['user','haj_steps']
    
    def update(self,instance,validated_data):
        user = instance.user
        phonenumber = validated_data.get('phonenumber')
        first_name = validated_data.get('first_name')
        last_name = validated_data.get('last_name')
        father_name = validated_data.get('father_name')
        grand_father = validated_data.get('grand_father')

        arrival_datetime = datetime.strptime(str(validated_data.get('arrival')), '%H:%M:%S')
        departure_datetime = datetime.strptime(str(validated_data.get('departure')), '%H:%M:%S')
        
        validated_data['duration'] = arrival_datetime - departure_datetime
        full_name = first_name+father_name+grand_father+last_name
        user.username = full_name
        user.first_name = first_name
        user.last_name = last_name
        user.phonenumber = phonenumber
        try:
            password = validated_data.pop('password')
            user.set_password(password)
        except:
            pass
        user.save()

        validated_data['user'] = user
        return super(UpdatePilgrimSerializer, self).update(instance, validated_data)





class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotification
        fields = '__all__'



class BaseNotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseNotification
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
    last_msg = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = '__all__'

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.user.image:
            return request.build_absolute_uri(obj.user.image.url)
        return None
    
    def get_last_msg(self,obj):
        try:
            msg = ChatMessage.objects.filter(chat=obj).order_by('-timestamp').first()
            return msg.content
        except:
            return ' '




class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioAttach
        fields = ['id','file']

    def to_representation(self, instance):
        request = self.context.get('request')
        representation = super().to_representation(instance)
        if instance.file:
            representation['file'] = request.build_absolute_uri(instance.file.url)
        return representation



class MessageSerializer(serializers.ModelSerializer):
    audio_url = serializers.SerializerMethodField()
    class Meta:
        model = ChatMessage
        fields = '__all__'

    def get_audio_url(self,obj):

        if obj.audio:
            return f"https://alnoor-hajj.com{obj.audio.file.url}"
        return None




class SimpleGuidancePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GuidancePost
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        content = representation.get('content', '')
        category_name = instance.category.name if instance.category else None
        representation['content'] = content[:60] + '...'
        representation['category_name'] = category_name
        return representation





class GuidancePostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GuidancePost
        fields = '__all__'




class SimpleReligiousPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReligiousPost
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        content = representation.get('content', '')
        category_name = instance.category.name if instance.category else None
        representation['content'] = content[:60] + "..."
        representation['category_name'] = category_name
        return representation
    



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



