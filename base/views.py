from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .serializers import *
from .models import *
from .filters import *
from .resources import *
from .permissions import *
from .notifications import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListAPIView  , CreateAPIView, UpdateAPIView, RetrieveAPIView , ListCreateAPIView , GenericAPIView
from .utils import get_response
from rest_framework import status
from datetime import datetime
from fcm_django.models import FCMDevice
from django.shortcuts import get_object_or_404
from fcm_django.models import FCMDevice
from firebase_admin.messaging import Message, Notification
from django.db.models import Max , Count
from django.db.models.functions import ExtractMonth


class LoginUser(GenericAPIView):

    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.get(phonenumber = request.data['username'])
        token = RefreshToken.for_user(user)


        device_token = request.data.get('device_token',None)
        # device_type = request.data.get('device_type',None)
        try:
            device_tok = FCMDevice.objects.get(registration_id=device_token ,type='android')
            device_tok.user = user
            device_tok.save()
        except:
            FCMDevice.objects.create(user=user , registration_id=device_token ,type='android')
    
        data = serializer.data
        try:
            guide_chat = Chat.objects.get(user=user, chat_type='guide')
            manager_chat = Chat.objects.get(user=user , chat_type='manager')
            data['guide_chat_id'] = guide_chat.id
            data['manager_chat_id'] = manager_chat.id
        except Chat.DoesNotExist:
            None


        data['image'] = request.build_absolute_uri(user.image.url)
        data['user_id'] = user.id
        try:
            pilgrim = Pilgrim.objects.get(user=user)
            data['pilgrim_id'] = pilgrim.id
        except Pilgrim.DoesNotExist:
            None

        data['tokens'] = {'refresh':str(token), 'access':str(token.access_token)}

        return Response(data, status=status.HTTP_200_OK)
    



class LogoutUser(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutUserSerializer

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
            chat = Chat.objects.get(user=user)
            msg = ChatMessage.objects.create(content=f'كود تغيير كلمة المرور هو {code}',employee=True)
            send_code(user=user,title='فريق الدعم',content='تم ارسال كود التحقق')
            return Response({'message':'تم ارسال رمز التحقق',
                             'user_id' : user.id})
        except:
            raise serializers.ValidationError({'error':'أدخل رقم هاتف صحيح'})
    




######### needs modification to adapt to sms
class VerifyCode(GenericAPIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        code = request.data['code']
        user = CustomUser.objects.get(id=pk)
        code_ver = VerificationCode.objects.filter(user=user.id).first()
        if code_ver:
            if str(code) == str(code_ver.code):
                if timezone.now() > code_ver.expires_at:
                    return Response({"message":"انتهت صلاحية رمز التحقق"}, status=status.HTTP_400_BAD_REQUEST)
                code_ver.is_verified = True
                code_ver.save()
                return Response({"message":"تم التحقق من الرمز", 'user_id':code_ver.user.id},status=status.HTTP_200_OK)
            else:
                return Response({'message':'الرمز خاطئ, يرجى إعادة إدخال الرمز بشكل صحيح'})
        


class UpdateImage(GenericAPIView):
    # permission_classes = [IsAuthenticated]

    def post(self,request):
        new_image = request.data['image'] or None
        if new_image is not None:
            user = request.user
            user.image = new_image
            user.save()
            serializer = CustomUserSerializer(user,many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":"اختر صورة من فضلك"} , status=status.HTTP_400_BAD_REQUEST)




######### needs modification to adapt to sms
class ResetPassword(UpdateAPIView):
    # permission_classes = [IsAuthenticated]
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



class RegisterPilgrim(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  Registration.objects.all()
    serializer_class = RegistrationSerializer



class ListCreatePilgrim(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Pilgrim.objects.all()
    serializer_class = PilgrimSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PilgrimFilter



class GetPilgrim(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Pilgrim.objects.all()
    serializer_class = PilgrimSerializer


class PilgrimInfo(GenericAPIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        user = request.user
        try:
            pilgrim = Pilgrim.objects.get(user=user)
            serializer = PilgrimSerializer(pilgrim , many=False)
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Pilgrim.DoesNotExist:
            return Response({"error":"لا يوجد حاج بهذا الاسم"},status=status.HTTP_500_BAD_REQUEST)




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



###### might meed modification to send the pilgrim id in the header
class ListNote(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NoteFilter




class CreateNote(APIView):
    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)




class RetUpdDesNote(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer


##### needs modification to send more info in the notification body
class ListNotifications(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  UserNotification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        notifications = UserNotification.objects.filter(user__id=user.id)
        return notifications
        


######## show all tasks or employee's tasks ????? asap
class ListTask(ListAPIView):
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



class RetUpdDesTask(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer



class CompleteTask(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer

    def post(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.completed = True
            task.save()
            serializer = TaskSerializer(task , many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error":"لا يوجد مهمة بهذا الرقم"},status=status.HTTP_400_BAD_REQUEST)
        



class AcceptTask(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer

    def post(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.accepted = True
            task.save()
            serializer = TaskSerializer(task , many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error":"لا يوجد مهمة بهذا الرقم"},status=status.HTTP_400_BAD_REQUEST)




class SendTask(GenericAPIView):
    # permission_classes = [IsAuthenticated]
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer

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







class CompleteStep(GenericAPIView):
    # permission_classes = [IsAuthenticated]

    def post(self,request,step_id):
        try:
            step = HajSteps.objects.get(id=step_id)
            pilgrim = Pilgrim.objects.get(user=request.user)
            if not pilgrim.haj_steps.filter(id=step.id).exists():
                pilgrim.haj_steps.add(step)
            else:
                pilgrim.haj_steps.remove(step)

            serializer = HajStepSerializer(step , many=False)
            return Response(serializer.data)
        except:
            return Response({"error":"لا يوجد خطوة بهذا الاسم"})





class ListHajSteps(ListAPIView):
    queryset = HajSteps.objects.all()
    serializer_class = HajStepSerializer
    # permission_classes = [IsAuthenticated]





class SendNotification(APIView):
    def post(self,request):
        pilgrims = Pilgrim.objects.values_list('user',flat=True)
        users = CustomUser.objects.filter(id__in = pilgrims)
        title = request.data.get('title')
        content = request.data.get('content')
        print(title)
        print(content)
        if pilgrims is not None:
            if title and content :
                send_event_notification(users=users,title=title,content=content)
                return Response({
                    "message":"تم ارسال الاشعار"
                })
            else:
                return Response({"error":"العنوان أو المحتوى فارغ"})
        else:
            return Response({"error":"لا يوجد حجاج"})



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

        # hijri_date = {
        #         'day': response['data']['date']['hijri']['day'],
        #         'month': response['data']['date']['hijri']['month']['ar'],
        #         'year': response['data']['date']['hijri']['year'],
        #         'weekday': response['data']['date']['hijri']['weekday']['ar'],
        #     }

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



class ListChats(ListCreateAPIView):
    querset = Chat.objects.all()
    serializer_class = ChatSerializer
    # permission_clasess = [IsGuide , IsAuthenticated]

    def get_queryset(self):
        chats = Chat.objects.annotate(latest_message_timestamp=Max('chatmessage__timestamp'))
        chats = chats.order_by('-latest_message_timestamp')
        return chats



class GetChat(RetrieveAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer



class ListEmployees(ListAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter


class CreateEmployee(CreateAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer 
   



class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = UpdateEmployeeSerializer 

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        employee_id = serializer.data['id']
        employee = Employee.objects.get(id=employee_id)
        serializer = EmployeeSerializer(employee , many=False , context={'request':request})
        return Response(serializer.data)






class ListCreateGuidancePost(ListCreateAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = GuidancePost.objects.all()
    serializer_class = SimpleGuidancePostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GuidancePostFilter


    

class RetUpdDesGuidancePost(RetrieveUpdateDestroyAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = GuidancePost.objects.all()
    serializer_class = GuidancePostSerializer


class ListCreateReligiousPost(ListCreateAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = ReligiousPost.objects.all()
    serializer_class = SimpleReligiousPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReligiousPostFilter


class RetUpdDesReligiousPost(RetrieveUpdateDestroyAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = ReligiousPost.objects.all()
    serializer_class = ReligiousPostSerializer


class ListCreateGuidanceCategory(ListCreateAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = GuidanceCategory.objects.all()
    serializer_class = GuidanceCategorySerializer




class RetUpdDesGuidanceCategory(RetrieveUpdateDestroyAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = GuidanceCategory.objects.all()
    serializer_class = GuidanceCategorySerializer


class ListCreateReligiousCategory(ListCreateAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = ReligiousCategory.objects.all()
    serializer_class = ReligiousCategorySerializer


class RetUpdDesReligiousCategory(RetrieveUpdateDestroyAPIView):
    # permission_clasess = [IsAuthenticated]
    queryset = ReligiousCategory.objects.all()
    serializer_class = ReligiousCategorySerializer








class LineChart(APIView):
    def get(self,request):
        year = datetime.now().year
        pilgrims = Pilgrim.objects.filter(created__year=year)\
                                        .annotate(month=ExtractMonth("created"))\
                                        .values("month").annotate(count=Count("id"))\
                                        .values("month", "count").order_by("month")
        serializer = ItemsPerMonthSerializer(pilgrims, many=True)
        return Response({
        "title": "الحجاج المسجلين حديثا",
        "data": {
            "datasets": [{
                "label": "Amount ($)",
                "backgroundColor": '#FFFFFF',
                "borderColor": '#FFFFFF',
                "data": serializer.data,
            }]
        },
    })
    








class PieChart(APIView): 
    def get(self,request):
        completed_tasks = Task.objects.filter(completed=True).values("completed").aggregate(Count('id'))['id__count']
        remaining_tasks = Task.objects.filter(completed=False).values("completed").aggregate(Count('id'))['id__count']
        return Response({
            "completed":completed_tasks,
            "remaining":remaining_tasks
        })
