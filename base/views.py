from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from .utils.filters import *
from .resources import *
from .utils.permissions import *
from .utils.notifications import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListAPIView  , CreateAPIView, UpdateAPIView, RetrieveAPIView , ListCreateAPIView , GenericAPIView
from .utils.utils import get_response
from rest_framework import status
from fcm_django.models import FCMDevice
from django.shortcuts import get_object_or_404
from fcm_django.models import FCMDevice
from rest_framework.views import APIView
from .utils.views import BaseAPIView


class LoginUser(GenericAPIView):
    def post(self, request):
        if request.data.get('username') and request.data.get('password'):
            serializer = LoginSerializer(data = request.data)

            if serializer.is_valid(raise_exception=True):
                user = CustomUser.objects.get(phonenumber = request.data['username'])
                token = RefreshToken.for_user(user)

                device_token = request.data.get('device_token',None)
                device_type = request.data.get('device_type','android')
                try:
                    device_tok = FCMDevice.objects.get(registration_id=device_token ,type=device_type)
                    device_tok.user = user
                    device_tok.save()
                except:
                    if device_token and device_token != '':
                        FCMDevice.objects.create(user=user , registration_id=device_token ,type='android')
                    else:
                        pass
                    
                data = serializer.data
                try:
                    guide_chat = Chat.objects.get(user=user, chat_type='guide')
                    data['guide_chat_id'] = guide_chat.id
                except Chat.DoesNotExist:
                    None
                    
                try:
                    manager_chat = Chat.objects.get(user=user , chat_type='manager')
                    data['manager_chat_id'] = manager_chat.id
                except Chat.DoesNotExist:
                    None

                data['image'] = request.build_absolute_uri(user.image.url)
                data['user_id'] = user.id
                data['user_type'] = user.user_type
                data['full_name'] = user.username
                try:
                    pilgrim = Pilgrim.objects.get(user=user)
                    data['pilgrim_id'] = pilgrim.id 
                    if pilgrim.guide:
                        data['guide_image'] = request.build_absolute_uri(pilgrim.guide.user.image.url) or None
                        data['guide_name'] = pilgrim.guide.user.username
                        data['guide_id'] = pilgrim.guide.user.id
                    else:
                        data['guide_id'] = 0
                except Pilgrim.DoesNotExist:
                    None

                data['tokens'] = {'refresh':str(token), 'access':str(token.access_token)}

                return Response(data, status=status.HTTP_200_OK)
            else:
                error_message = ', '.join(serializer.errors.values())
                return Response({'error': serializer.errors.values()}, status=400)    
        else:
            return Response({"error":["لا يمكن أن تكون الحقول فارغة"]} , status=status.HTTP_400_BAD_REQUEST)


class LogoutUser(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LogoutUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)




class VerifyUser(APIView):
    def post(self,request):
        registration_id = request.data['registration_id'] or None
        phonenumber = request.data['phonenumber'] or None

        if registration_id and phonenumber:
            try:
                Pilgrim.objects.get(registration_id=registration_id , phonenumber=phonenumber, user__is_deleted=False)
                return Response({"success":"تم التحقق من هوية المستخدم"} , status=status.HTTP_200_OK)
            except Pilgrim.DoesNotExist:
                return Response({"error":"لا يوجد حاج بهذه المعلومات"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error":"الرجاء إدخال رقم الهاتف و رقم الهوية"}, status=status.HTTP_400_BAD_REQUEST)








class UpdateImage(BaseAPIView):
    def post(self,request):
        new_image = request.data['image'] or None
        if new_image is not None:
            user = request.user
            user.image = new_image
            user.save()
            serializer = CustomUserSerializer(user,many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error":["اختر صورة من فضلك"]} , status=status.HTTP_400_BAD_REQUEST)



### can be addes to the models as  a method
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
            return Response({'error':['ليس لديك صلاحية لتغيير كلمة المرور']})



class RegisterPilgrim(ListCreateAPIView):
    queryset =  Registration.objects.all()
    serializer_class = RegistrationSerializer




class ListPilgrim(ListAPIView):
    queryset = Pilgrim.objects.select_related('guide','user').prefetch_related('haj_steps').filter(user__is_deleted=False)
    serializer_class = ListPilgrimSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PilgrimFilter



class ListGuidePilgrims(ListAPIView, BaseAPIView):
    queryset = Pilgrim.objects.all()
    serializer_class = PilgrimSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = PilgrimFilter

    def get_queryset(self):
        user = self.request.user
        pilgrims = Pilgrim.objects.filter(guide__user=user , user__is_deleted=False)
        return pilgrims



class CreatePilgrim(CreateAPIView):
    queryset = Pilgrim.objects.all()
    serializer_class = CreatePilgrimSerializer




class UpdatePilgrim(UpdateAPIView):
    queryset = Pilgrim.objects.all()
    serializer_class = UpdatePilgrimSerializer




class PilgrimSteps(APIView):
    def get(self,request,pilgrim_id):
        try:
            pilgrim = Pilgrim.objects.get(id=pilgrim_id, user__is_deleted=False)
            steps = HaJStepsPilgrim.objects.filter(pilgrim=pilgrim)
            serializer = CompletedHajStepsPilgrimSerializer(steps , many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        except Pilgrim.DoesNotExist:
            return Response({"error":"لا يوجد حاج بهذا الرقم"})



class GetPilgrim(RetrieveUpdateDestroyAPIView):
    queryset = Pilgrim.objects.all()
    serializer_class = PilgrimSerializer



class DeletePilgrims(GenericAPIView):
    def delete(self,request):
        pilgrims = Pilgrim.objects.all()
        if pilgrims:
            pilgrims.update(is_deleted=True)
            return Response({"msg":"all pilgrim accounts deleted successfully"})
        else:
            return Response({"error":"there are no pilgrims registered"})




class UpdatePilgrimLocation(GenericAPIView):
    def post(self,request,pk):
        long = request.data.get('long',None)
        lat = request.data.get('lat',None)
        if long and lat:
            try:
                pilgrim = Pilgrim.objects.get(id=pk, user__is_deleted=False)
                pilgrim.longitude = long
                pilgrim.latitude = lat
                pilgrim.save()
                return Response({"msg":"location updated successflly."})
            except Pilgrim.DoesNotExist:
                return Response({"error":"pilgrim does not exist"})
        else:
            return Response({"error":"please provide correct values for longitude and latitude"})


class RefreshFirebaseToken(GenericAPIView):

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


class ListNote(ListAPIView):
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = NoteFilter




class CreateNote(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = NoteSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class GetPilgrimNotes(APIView):
    def get(self,reuquest,pk):
        try:
            pilgrim = Pilgrim.objects.get(id=pk, user__is_deleted=False)
            notes = Note.objects.filter(pilgrim=pilgrim.id)
            serializer = NoteSerializer(notes , many=True)
            return Response(serializer.data , status=status.HTTP_200_OK)
        
        except Pilgrim.DoesNotExist:
            return Response({"error":'Pilgrim does not exist'} , status=status.HTTP_404_NOT_FOUND)





class RetUpdDesNote(RetrieveUpdateDestroyAPIView):
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer


class ListNotifications(ListAPIView, BaseAPIView):
    queryset =  UserNotification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        user = self.request.user
        notifications = UserNotification.objects.filter(user__id=user.id)
        return notifications
        


class ListBaseNotifications(ListAPIView, BaseAPIView):
    queryset = BaseNotification.objects.all()
    serializer_class = BaseNotificationSerializer

    def get_queryset(self,request):
        user = request.user
        notifications = BaseNotification.objects.filter(sentBy=user)
        return notifications


class ListTask(ListAPIView, BaseAPIView):
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
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer



class CompleteTask(GenericAPIView):
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
            return Response({"error":["لا يوجد مهمة بهذا الرقم"]},status=status.HTTP_400_BAD_REQUEST)
        



class AcceptTask(GenericAPIView):
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer

    #### put the accept task in the model
    def post(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.accepted = True
            task.save()
            serializer = TaskSerializer(task , many=False)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except Task.DoesNotExist:
            return Response({"error":["لا يوجد مهمة بهذا الرقم"]},status=status.HTTP_400_BAD_REQUEST)




class SendTask(GenericAPIView):
    queryset =  Task.objects.all()
    serializer_class = TaskSerializer

    def post(self,request,pk):
        try:
            employee = Employee.objects.get(id=pk)
            title = request.data.get('title',None)
            content = request.data.get('content',None)
            if title is None or content is None:
                return Response({"error" : ["العنوان أو المحتوى فارغ"]},status=status.HTTP_400_BAD_REQUEST)
            
            else:
                task = Task.objects.create(
                    employee = employee,
                    title = title,
                    content  = content,
                )
                send_task_notification(employee=employee,title="لديك مهمة جديدة",content=content)
                serializer = TaskSerializer(task , many=False)
                return Response(serializer.data , status=status.HTTP_200_OK)
        except Employee.DoesNotExist:
            return Response({"error":["لا يوجد موظف بهذا الرقم"]},status=status.HTTP_404_NOT_FOUND)






class CompleteStep(BaseAPIView):
    def post(self,request,step_id):
        try:
            completed = False
            step = HajSteps.objects.get(id=step_id)
            pilgrim = Pilgrim.objects.get(user=request.user, user__is_deleted=False)
            if not pilgrim.haj_steps.filter(id=step.id).exists():
                pilgrim.haj_steps.add(step)
                completed = True
            else:
                pilgrim.haj_steps.remove(step)

            serializer = HajStepSerializer(step , many=False)
            return Response({
                'id':serializer.data['id'],
                'scondary_steps':serializer.data['secondary_steps'],
                'name':serializer.data['name'],
                'rank':serializer.data['rank'],
                'note':serializer.data['note'],
                'completed':completed,

            } , status=status.HTTP_200_OK)
        
        except HajSteps.DoesNotExist:
            return Response({"error":"لا يوجد خطوة بهذا الاسم"} , status=status.HTTP_404_DOES_NOT_EXIST)






class ListHajSteps(BaseAPIView):
    def get(self,request):
        response_data = []
        pilgrim = Pilgrim.objects.get(user=request.user , user__is_deleted=False)
        steps = HaJStepsPilgrim.objects.filter(pilgrim=pilgrim).values('haj_step__name')
        serializer = HajStepsPilgrimSerializer(steps , many=True)

        total_steps = HajSteps.objects.all()
        total_serializer = HajStepSerializer(total_steps,many=True)

        for step in total_serializer.data:
            if HaJStepsPilgrim.objects.filter(Q(pilgrim=pilgrim) & Q(haj_step=step['id'])).exists():
                response_data.append({
                    'id':step['id'],
                    'scondary_steps':step['secondary_steps'],
                    'name':step['name'],
                    'rank':step['rank'],
                    'note':step['note'],
                    'completed':True,
                })
            else:
                response_data.append({
                    'id':step['id'],
                    'secondary_steps':step['secondary_steps'],
                    'name':step['name'],
                    'rank':step['rank'],
                    'note':step['note'],
                    'completed':False,
                })

        return Response(response_data , status=status.HTTP_200_OK)






class SendNotification(APIView):
    permission_classes = [IsAuthenticated]

    def post(self,request):
        user = request.user
        pilgrims = Pilgrim.objects.all().exists()
        title = request.data.get('title')
        content = request.data.get('content')
        if pilgrims:
            if title and content :
                if user.user_type == 'مرشد':
                    send_pilgrims_notification(title=title,content=content,sentBy=user)
                elif user.user_type == 'اداري':
                    send_event_notification(title=title,content=content)
                return Response({
                    "message":"تم ارسال الاشعار"
                })
            else:
                return Response({"error":["العنوان أو المحتوى فارغ"]})
        else:
            return Response({"error":["لا يوجد حجاج"]})




class Calender(APIView):
    def post(self,request):
        longitude = request.data.get('longitude')
        latitude = request.data.get('latitude')
        day = request.data.get('day')
        month = request.data.get('month')
        year = request.data.get('year')
        time = request.data.get('time',None)


        response = get_response(longitude,latitude,day,month,year)
        gregorian_date = {
            'day': response['data']['date']['gregorian']['day'],
            'month': response['data']['date']['gregorian']['month']['en'],
            'year': response['data']['date']['gregorian']['year'],
        }

        gregorian = GregorianSerializer(gregorian_date)
        arabic_gregorian_date = gregorian.data

        if time is not None:
            next_prayer = get_next_prayer(response['data']['timings'] , time)
        else:
            next_prayer = None

        return Response({
            'timings': response['data']['timings'],
            'next_prayer' : next_prayer,
            'gregorian': arabic_gregorian_date,
            'city': response['data']['meta']['timezone']
        })





class ListChats(ListCreateAPIView):
    querset = Chat.objects.all()
    serializer_class = ChatSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ChatFilter
    permission_clasess = [IsAuthenticated]

    def get_queryset(self):
        guide = Guide.objects.get(user=self.request.user)
        users = Pilgrim.objects.filter(guide=guide, user__is_deleted=False).values_list('user',flat=True)
        return Chat.guide_chats.filter(user__in=users)





class ListManagerChats(ListCreateAPIView):
    querset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_queryset(self):
        return Chat.manager_chats



class GetChat(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer





class ListGuides(ListAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer




class GetGuide(RetrieveAPIView):
    queryset = Guide.objects.all()
    serializer_class = GuideSerializer




class UploadAudio(APIView):
    def post(self,request):
        serializer = AudioSerializer(data=request.data , context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        else:
            return Response({"error":["error uploading audio"]} , status=status.HTTP_400_BAD_REQUEST)



class DeleteUserView(APIView):
    def delete(self,request,pk):
        user = CustomUser.objects.get(id=pk)
        user.is_deleted = True
        user.save()
        
        # Blacklist all refresh tokens for this user
        tokens = OutstandingToken.objects.filter(user_id=user.id)
        for token in tokens:
            BlacklistedToken.objects.get_or_create(token=token)
            
        return Response({"message":"user deleted successfully"} , status=status.HTTP_200_OK)



class SetActive(APIView):
    def post(self,request,user_id):
        try:
            user = CustomUser.objects.get(id=user_id)
            user.active_now = request.data['state']
            user.save()
            serializer = CustomUserSerializer(user,many=False)
            return Response(serializer.data , status=status.HTTP_200_OK)

        except CustomUser.DoesNotExist:
            return Response({"error":["لا يوجد مستخدم بهذا الرقم"]})



class ListEmployees(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = EmployeeFilter




class GetEmployee(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



class CreateEmployee(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = CreateEmployeeSerializer

   
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        employee_id = serializer.data['id']
        employee = Employee.objects.get(id=employee_id)
        serializer = EmployeeSerializer(employee , many=False , context={'request':request})
        return Response(serializer.data)



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
    queryset = GuidancePost.objects.all()
    serializer_class = SimpleGuidancePostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GuidancePostFilter


    

class RetUpdDesGuidancePost(RetrieveUpdateDestroyAPIView):
    queryset = GuidancePost.objects.all()
    serializer_class = GuidancePostSerializer


class ListCreateReligiousPost(ListCreateAPIView):
    queryset = ReligiousPost.objects.all()
    serializer_class = SimpleReligiousPostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReligiousPostFilter


class RetUpdDesReligiousPost(RetrieveUpdateDestroyAPIView):
    queryset = ReligiousPost.objects.all()
    serializer_class = ReligiousPostSerializer


class ListCreateGuidanceCategory(ListCreateAPIView):
    queryset = GuidanceCategory.objects.all()
    serializer_class = GuidanceCategorySerializer




class RetUpdDesGuidanceCategory(RetrieveUpdateDestroyAPIView):
    queryset = GuidanceCategory.objects.all()
    serializer_class = GuidanceCategorySerializer


class ListCreateReligiousCategory(ListCreateAPIView):
    queryset = ReligiousCategory.objects.all()
    serializer_class = ReligiousCategorySerializer


class RetUpdDesReligiousCategory(RetrieveUpdateDestroyAPIView):
    queryset = ReligiousCategory.objects.all()
    serializer_class = ReligiousCategorySerializer



class ListLiveStream(ListCreateAPIView):
    queryset = LiveStream.objects.all()
    serializer_class = LiveStreamSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = LiveStreamFilter

class RetUpdDesLiveStream(RetrieveUpdateDestroyAPIView):
    queryset = LiveStream.objects.all()
    serializer_class = LiveStreamSerializer

class ListCreateStreamType(ListCreateAPIView):
    queryset = LiveStreamCategory.objects.all()
    serializer_class = LiveStreamTypeSerializer

class RetUpdDesStreamType(RetrieveUpdateDestroyAPIView):
    queryset = LiveStreamCategory.objects.all()
    serializer_class = LiveStreamTypeSerializer




