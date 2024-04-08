from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
from .filters import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView , ListAPIView , RetrieveAPIView , ListCreateAPIView , GenericAPIView
from .utils import get_response
from rest_framework import status
from datetime import datetime
from fcm_django.models import FCMDevice




class LoginUserApiView(GenericAPIView):

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
    



class LogoutUserAPIView(GenericAPIView):
    serializer_class = LogoutUserSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)




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



class ListCreateNote(ListCreateAPIView):
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer


class RetUpdDesNote(RetrieveUpdateDestroyAPIView):
    queryset =  Note.objects.all()
    serializer_class = NoteSerializer


class ListNotifications(ListAPIView):
    queryset =  Notification.objects.all()
    serializer_class = NotificationSerializer
    




class CalenderView(APIView):
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



class Chats(APIView):
    def get(self,request):
        chats = Chat.objects.all()
        print(request.encoding)
        serializer = ChatSerializer(chats,many=True, context={'request': request})
        return Response(serializer.data , status=status.HTTP_200_OK)
    


class GetChat(RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
