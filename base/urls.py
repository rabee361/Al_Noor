from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/login/' , LoginUser.as_view() , name="login"),
    path('auth/logout/', LogoutUser.as_view(), name='logout'),
    path('send-code/' , SendCodePassword.as_view() , name="send-code"),
    path('verify-code/<str:pk>/' , VerifyCode.as_view() , name="verify-code"),
    path('auth/reset-password/<str:user_id>/' , ResetPassword.as_view(), name='reset-password'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('firebase-token/refresh/',RefreshFirebaseToken.as_view(),name="refresh-firebase-token"),
    path('prayers-timings/' , Calender.as_view() , name="prayers-timings"),
    path('list-notes/' , ListCreateNote.as_view() , name="list-notes"),
    path('get-note/' , RetUpdDesNote.as_view() , name="get-note"),
    path('list-tasks/' , ListCreateTask.as_view() , name="list-tasks"),
    path('get-task/' , RetUpdDesTask.as_view() , name="get-task"),
    path('list-chats/' , ListChats.as_view() , name="list-chats"),
    path('send-task/<str:pk>/' , SendTask.as_view() , name="send-task"),
    path('send-notification/' , SendNotification.as_view() , name="send-notification"),




    
    # path('list-notifications/' , )
]
