from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/login/' , LoginUser.as_view() , name="login"),
    path('auth/logout/', LogoutUser.as_view(), name='logout'),
    path('register/' , RegisterPilgrim.as_view() , name="register-pilgrim"),
    path('update-image/' , UpdateImage.as_view() , name="update-image"),
    path('send-code/' , SendCodePassword.as_view() , name="send-code"),
    path('verify-code/<str:pk>/' , VerifyCode.as_view() , name="verify-code"),
    path('auth/reset-password/<str:user_id>/' , ResetPassword.as_view(), name='reset-password'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('firebase-token/refresh/',RefreshFirebaseToken.as_view(),name="refresh-firebase-token"),
    path('prayers-timings/' , Calender.as_view() , name="prayers-timings"),
    path('list-chats/' , ListChats.as_view() , name="list-chats"),
    path('list-manager-chats/' , ListManagerChats.as_view() , name="list-chats"),
    path('get-chat/<str:pk>/' , GetChat.as_view() , name="get-chat"),
    path('create-note/' , CreateNote.as_view() , name="create-note"),
    path('list-notes/' , ListNote.as_view() , name="list-notes"),
    path('list-guides/' , ListGuides.as_view() , name="list-guides"),
    path('get-note/<str:pk>/' , RetUpdDesNote.as_view() , name="get-note"),
    path('list-tasks/' , ListTask.as_view() , name="list-tasks"),
    path('get-task/<str:pk>/' , RetUpdDesTask.as_view() , name="get-task"),
    path('complete-task/<str:task_id>/' , CompleteTask.as_view() , name="complete-task"),
    path('accept-task/<str:task_id>/' , AcceptTask.as_view() , name="accept-task"),
    path('send-task/<str:pk>/' , SendTask.as_view() , name="send-task"),
    path('list-notifications/' , ListNotifications.as_view() , name="list-notifications"),
    path('send-notification/' , SendNotification.as_view() , name="send-notification"),
    path('list-pilgrims/' , ListPilgrim.as_view() , name="list-pilgrims"),
    path('create-pilgrim/' , CreatePilgrim.as_view() , name="create-pilgrim"),
    path('update-pilgrim/<str:pk>/' , UpdatePilgrim.as_view() , name="update-pilgrim"),
    path('get-pilgrim/<str:pk>/' , GetPilgrim.as_view() , name="get-pilgrim"),
    path('create-employee/' , CreateEmployee.as_view() , name="create-employee"),
    path('get-employee/<str:pk>/' , GetEmployee.as_view() , name="get-employee"),
    path('list-employees/' , ListEmployees.as_view() , name="list-employees"),
    path('update-employee/<str:pk>/' , UpdateEmployee.as_view() , name="update-employee"),
    path('complete-step/<str:step_id>/' , CompleteStep.as_view() , name="complete-step"),
    path('list-steps/' , ListHajSteps.as_view() , name="haj-steps"),
    path('religious-categories/' , ListCreateReligiousCategory.as_view() , name="list-religious-categories"),
    path('religious-category/<str:pk>/' , RetUpdDesReligiousCategory.as_view() , name="get-religious-category"),
    path('guidance-categories/' , ListCreateGuidanceCategory.as_view() , name="list-guidance-categories"),
    path('guidance-category/<str:pk>/' , RetUpdDesGuidanceCategory.as_view() , name="get-guidance-category"),
    path('religious-posts/' , ListCreateReligiousPost.as_view() , name="list-religious-posts"),
    path('religious-post/<str:pk>/' , RetUpdDesReligiousPost.as_view() , name="get-religious-post"),
    path('guidance-posts/' , ListCreateGuidancePost.as_view() , name="list-guidance-posts"),
    path('guidance-post/<str:pk>/' , RetUpdDesGuidancePost.as_view() , name="get-guidance-post"),
    path('set-active/<str:pilgrim_id>/' , SetActive.as_view() , name="set-active"),

    # path('chart/options/', GetOptions.as_view(), name="options"),
    path('chart/line-chart/', LineChart.as_view() , name="line-chart"),
    path('chart/pie-chart/' , PieChart.as_view() , name="pie-chart"),

]
