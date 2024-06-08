from django.urls import path , include
from .views import *
from rest_framework_simplejwt import views as jwt_views


# General api's for each user type 
AccountPattern = [
    path('auth/login/' , LoginUser.as_view() , name="login"),
    path('auth/logout/', LogoutUser.as_view(), name='logout'),
    path('list-notifications/' , ListNotifications.as_view() , name="list-notifications"),
    path('update-image/' , UpdateImage.as_view() , name="update-image"),
    path('send-code/' , SendCodePassword.as_view() , name="send-code"),
    path('verify-user/' , VerifyUser.as_view() , name="verify-user"),
    path('auth/reset-password/<str:user_id>/' , ResetPassword.as_view(), name='reset-password'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('firebase-token/refresh/',RefreshFirebaseToken.as_view(),name="refresh-firebase-token"),
    path('set-active/<str:user_id>/' , SetActive.as_view() , name="set-active")
]


# Pilgrim app api's
PilgrimPattern = [
    path('complete-step/<str:step_id>/' , CompleteStep.as_view() , name="complete-step"),
    path('prayers-timings/' , Calender.as_view() , name="prayers-timings"),
    path('register/' , RegisterPilgrim.as_view() , name="register-pilgrim"),
    path('list-steps/' , ListHajSteps.as_view() , name="haj-steps"),
    path('religious-categories/' , ListCreateReligiousCategory.as_view() , name="list-religious-categories"),
    path('religious-category/<str:pk>/' , RetUpdDesReligiousCategory.as_view() , name="get-religious-category"),
    path('guidance-categories/' , ListCreateGuidanceCategory.as_view() , name="list-guidance-categories"),
    path('guidance-category/<str:pk>/' , RetUpdDesGuidanceCategory.as_view() , name="get-guidance-category"),
    path('religious-posts/' , ListCreateReligiousPost.as_view() , name="list-religious-posts"),
    path('religious-post/<str:pk>/' , RetUpdDesReligiousPost.as_view() , name="get-religious-post"),
    path('guidance-posts/' , ListCreateGuidancePost.as_view() , name="list-guidance-posts"),
    path('guidance-post/<str:pk>/' , RetUpdDesGuidancePost.as_view() , name="get-guidance-post")
]


# Manager app api's
ManagerPattern = [
    path('list-manager-chats/' , ListManagerChats.as_view() , name="list-chats"),
    path('send-task/<str:pk>/' , SendTask.as_view() , name="send-task"),
    path('list-chats/' , ListChats.as_view() , name="list-chats"),
    path('get-chat/<str:pk>/' , GetChat.as_view() , name="get-chat"),
    path('send-notification/' , SendNotification.as_view() , name="send-notification"),
    path('list-pilgrims/' , ListPilgrim.as_view() , name="list-pilgrims"),
    path('create-employee/' , CreateEmployee.as_view() , name="create-employee"),
    path('get-employee/<str:pk>/' , GetEmployee.as_view() , name="get-employee"),
    path('list-employees/' , ListEmployees.as_view() , name="list-employees"),
    path('update-employee/<str:pk>/' , UpdateEmployee.as_view() , name="update-employee"),
    path('get-pilgrim/<str:pk>/' , GetPilgrim.as_view() , name="get-pilgrim"),
    path('get-note/<str:pk>/' , RetUpdDesNote.as_view() , name="get-note"),
    path('delete-note/<str:pk>/' , RetUpdDesNote.as_view() , name="delete-note"),
    path('update-note/<str:pk>/' , RetUpdDesNote.as_view() , name="update-note"),
    path('list-guides/' , ListGuides.as_view() , name="list-guides"),
    path('create-pilgrim/' , CreatePilgrim.as_view() , name="create-pilgrim"),
    path('update-pilgrim/<str:pk>/' , UpdatePilgrim.as_view() , name="update-pilgrim"),
    path('list-all-guides/' , get_pilgrims , name="get-all-pilgrims"),    
]


# Employee app api's
EmployeePattern = [
    path('complete-task/<str:task_id>/' , CompleteTask.as_view() , name="complete-task"),
    path('accept-task/<str:task_id>/' , AcceptTask.as_view() , name="accept-task"),
    path('list-tasks/' , ListTask.as_view() , name="list-tasks"),
    path('get-task/<str:pk>/' , RetUpdDesTask.as_view() , name="get-task"),

]


# guide app api's
GuidePattern = [
    path('create-note/' , CreateNote.as_view() , name="create-note"),
    path('list-notes/' , ListNote.as_view() , name="list-notes"),
    path('list-chats/' , ListChats.as_view() , name="list-chats"),
    path('get-chat/<str:pk>/' , GetChat.as_view() , name="get-chat"),
    path('send-notification/' , SendNotification.as_view() , name="send-notification"),
    path('list-guide-pilgrims/' , ListGuidePilgrims.as_view() , name="list-guide-pilgrims"),
    path('get-pilgrim/<str:pk>/' , GetPilgrim.as_view() , name="get-pilgrim"),
    path('get-note/<str:pk>/' , RetUpdDesNote.as_view() , name="get-note"),
    path('delete-note/<str:pk>/' , RetUpdDesNote.as_view() , name="delete-note"),
    path('update-note/<str:pk>/' , RetUpdDesNote.as_view() , name="update-note")
]


urlpatterns = [
    path('' , include(AccountPattern)),
    path('' , include(PilgrimPattern)),
    path('' , include(ManagerPattern)),
    path('' , include(EmployeePattern)),
    path('' , include(GuidePattern))
]
