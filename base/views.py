from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .filters import *
from .notifications import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListAPIView , UpdateAPIView, RetrieveAPIView , ListCreateAPIView , GenericAPIView
from .utils import get_response
from rest_framework import status
from datetime import datetime
from fcm_django.models import FCMDevice
from django.shortcuts import get_object_or_404




class LoginUser(GenericAPIView):

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.get(phonenumber = request.data['username'])
        token = RefreshToken.for_user(user)

        chat = Chat.objects.filter(user=user).first()
        data = serializer.data
        if chat:
            data['chat_id'] = chat.id

        data['image'] = request.build_absolute_uri(user.image.url)
        data['id'] = user.id
        data['tokens'] = {'refresh':str(token), 'access':str(token.access_token)}

        return Response(data, status=status.HTTP_200_OK)
    



class LogoutUser(GenericAPIView):
    serializer_class = LogoutUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)



######### needs modification to adapt to sms
class SendCodePassword(GenericAPIView):
    def post(self, request):
        try: 
            phonenumber = request.data['phonenumber']
            user = get_object_or_404(CustomUser, phonenumber=phonenumber)
            existing_code = VerificationCode.objects.filter(user=user).first()
            if existing_code:
                existing_code.delete()
            code_verivecation = generate_code()
            code = VerificationCode.objects.create(user=user, code=code_verivecation)
            return Response({'message':'تم ارسال رمز التحقق',
                             'user_id' : user.id})
        except:
            raise serializers.ValidationError({'error':'pleace enter valid phonenumber'})
    




######### needs modification to adapt to sms
class VerifyCode(GenericAPIView):

    def post(self, request, pk):
        code = request.data['code']
        user = CustomUser.objects.get(id=pk)
        code_ver = VerificationCode.objects.filter(user=user.id).first()
        if code_ver:
            if str(code) == str(code_ver.code):
                if timezone.now() > code_ver.expires_at:
                    return Response({"message":"Verification code has expired"}, status=status.HTTP_400_BAD_REQUEST)
                code_ver.is_verified = True
                code_ver.save()
                return Response({"message":"تم التحقق من الرمز", 'user_id':code_ver.user.id},status=status.HTTP_200_OK)
            else:
                return Response({'message':'الرمز خاطئ, يرجى إعادة إدخال الرمز بشكل صحيح'})
        




######### needs modification to adapt to sms
class ResetPassword(UpdateAPIView):
    serializer_class = ResetPasswordSerializer

    def put(self, request, user_id):
        user = CustomUser.objects.get(id=user_id)
        if user.is_verified:
            data = request.data
            serializer = self.get_serializer(data=data, context={'user_id':user_id})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            messages = {
                'message':'تم تغيير كلمة المرور بنجاح'
            }
            return Response(messages, status=status.HTTP_200_OK)
        
        else:
            return Response({'error':'ليس لديك صلاحية لتغيير كلمة المرور'})



class RefreshFirebaseToken(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    def post(self,request):
        token = request.data['firebase-token']
        user_id = request.data['user_id']
        try:
            user = CustomUser.objects.get(id=user_id)
            device = FCMDevice.objects.get(user=user)
            device.registration_id = token
            device.save()
        except:
            raise CustomUser.DoesNotExist

        return Response({
            "msg" : "firebase token changed successfully"
        },status=status.HTTP_200_OK)




class ListChats(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer




class ListCreateNote(ListCreateAPIView):
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer


class RetUpdDesNote(RetrieveUpdateDestroyAPIView):
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer



class ListNotifications(GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        notification = UserNotification.objects.filter(user__id=user.id)
        serializer = NotificationSerializer(notification, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        



class ListCreateTask(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        user = self.request.user
        if not user:
            return Task.objects.none()
        else:
            employee = Employee.objects.get(user=user)
            return Task.objects.filter(employee=employee)



class RetUpdDesTask(ListCreateAPIView):
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer



class SendTask(GenericAPIView):
    def post(self,request,pk):
        employee = Employee.objects.get(id=pk)
        title = request.data.get('title',None)
        content = request.data.get('content',None)
        if title is None or content is None:
            return Response({"error" : "العنوان أو المحتوى فارغ"},status=status.HTTP_400_BAD_REQUEST)
        
        else:
            task = Task.objects.create(
                employee = employee,
                title = title,
                content  = content,
            )
            send_task_notification(employee=employee,title=title,content=content)
            serializer = TaskSerializer(task , many=False)
            return Response(serializer.data , status=status.HTTP_200_OK)




class SendNotification(GenericAPIView):
    def post(self,request):
        users = CustomUser.objects.filter()
        if title is None or content is None:
            title = request.data.get('title',None)
            content = request.data.get('content',None)
            send_event_notification(title=title,content=content)
            return Response({
                "message":"تم ارسال الاشعار"
            })
        else:
            return Response({"error":"العنوان أو المحتوى فارغ"})


class Calender(GenericAPIView):
    def post(self,request):
        longitude = request.data.get('longitude')
        latitude = request.data.get('latitude')
        day = request.data.get('day')
        month = request.data.get('month')
        year = request.data.get('year')

        response = get_response(longitude,latitude,day,month,year)
        gregorian_date = {
            'day': response['data']['date']['gregorian']['day'],
            'month': response['data']['date']['gregorian']['month']['en'],
            'year': response['data']['date']['gregorian']['year'],
        }

        hijri_date = {
                'day': response['data']['date']['hijri']['day'],
                'month': response['data']['date']['hijri']['month']['ar'],
                'year': response['data']['date']['hijri']['year'],
                'weekday': response['data']['date']['hijri']['weekday']['ar'],
            }

        gregorian = GregorianSerializer(gregorian_date)
        hijri = HijriSerializer(hijri_date)
        arabic_gregorian_date = gregorian.data
        arabic_hijri_date = hijri.data

        return Response({
            'timings': response['data']['timings'],
            'hijri' : arabic_hijri_date,
            'gregorian': arabic_gregorian_date,
            'city': response['data']['meta']['timezone']
        })



class Chats(GenericAPIView):
    def get(self,request):
        chats = Chat.objects.all()
        serializer = ChatSerializer(chats,many=True, context={'request': request})
        return Response(serializer.data , status=status.HTTP_200_OK)
    


class GetChat(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer



class ListCreateGuidancePost(ListCreateAPIView):
    queryset = GuidancePost.objects.all()
    serializer_class = GuidancePostSerializer


class RetUpdDesGuidancePost(ListCreateAPIView):
    queryset = GuidancePost.objects.all()
    serializer_class = GuidancePostSerializer


class ListCreateReligiousPost(ListCreateAPIView):
    queryset = ReligiousPost.objects.all()
    serializer_class = ReligiousPostSerializer


class RetUpdDesReligiousPost(ListCreateAPIView):
    queryset = ReligiousPost.objects.all()
    serializer_class = ReligiousPostSerializer



class ListCreateGuidanceCategory(ListCreateAPIView):
    queryset = GuidanceCategory.objects.all()
    serializer_class = GuidanceCategorySerializer


class RetUpdDesGuidanceCategory(ListCreateAPIView):
    queryset = GuidanceCategory.objects.all()
    serializer_class = GuidanceCategorySerializer


class ListCreateReligiousCategory(ListCreateAPIView):
    queryset = ReligiousCategory.objects.all()
    serializer_class = ReligiousCategorySerializer


class RetUpdDesReligiousCategory(ListCreateAPIView):
    queryset = ReligiousCategory.objects.all()
    serializer_class = ReligiousCategorySerializer