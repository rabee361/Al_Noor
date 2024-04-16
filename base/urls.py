from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('settings/update-image/<str:pk>/', UpdateImageView.as_view(), name='update-image'),
    path('auth/login/' , LoginUser.as_view() , name="login"),
    path('auth/logout/', LogoutUser.as_view(), name='logout'),
    path('register/' , RegisterPilgrim.as_view() , name="register-pilgrim"),
    path('send-code/' , SendCodePassword.as_view() , name="send-code"),
    path('verify-code/<str:pk>/' , VerifyCode.as_view() , name="verify-code"),
    path('auth/reset-password/<str:user_id>/' , ResetPassword.as_view(), name='reset-password'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('firebase-token/refresh/',RefreshFirebaseToken.as_view(),name="refresh-firebase-token"),
    path('prayers-timings/' , Calender.as_view() , name="prayers-timings"),
    path('list-chats/' , ListChats.as_view() , name="list-chats"),
    path('list-notes/' , ListCreateNote.as_view() , name="list-notes"),
    path('get-note/' , RetUpdDesNote.as_view() , name="get-note"),
    path('list-tasks/' , ListCreateTask.as_view() , name="list-tasks"),
    path('get-task/' , RetUpdDesTask.as_view() , name="get-task"),
    path('send-task/<str:pk>/' , SendTask.as_view() , name="send-task"),
    path('list-notifications/' , ListNotifications.as_view() , name="list-notifications"),
    path('send-notification/' , SendNotification.as_view() , name="send-notification"),
    path('religious-categories/' , ListCreateReligiousCategory.as_view() , name="list-religious-categories"),
    path('religious-category/<str:pk>/' , RetUpdDesReligiousCategory.as_view() , name="get-religious-category"),
    path('guidance-categories/' , ListCreateGuidanceCategory.as_view() , name="list-guidance-categories"),
    path('guidance-category/<str:pk>/' , RetUpdDesGuidanceCategory.as_view() , name="get-guidance-category"),
    path('religious-posts/' , ListCreateReligiousPost.as_view() , name="list-religious-posts"),
    path('religious-post/<str:pk>/' , RetUpdDesReligiousPost.as_view() , name="get-religious-post"),
    path('guidance-posts/' , ListCreateGuidancePost.as_view() , name="list-guidance-posts"),
    path('guidance-post/<str:pk>/' , RetUpdDesGuidancePost.as_view() , name="get-guidance-post"),
    path('employee/' , ListCreateEmployee.as_view() , name="create"),
    path('export/pilgrim/', export_pilgram, name='export_pilgrim'),

    ################################3
    path('list-create-pilgrim/', ListCreatePilgrimView.as_view(), name='list-create-pilgrim'),
    path('get-info-flow/', GetUpdateInfoFlowView.as_view(), name='get-info-flow'),
]
