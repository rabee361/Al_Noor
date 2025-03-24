from django.urls import path , include
from .views import *
from rest_framework_simplejwt import views as jwt_views


# General endpoints for all users
AccountPatterns = [
    path('auth/login/' , LoginUser.as_view()),
    path('auth/logout/', LogoutUser.as_view()),
    path('list-notifications/' , ListNotifications.as_view()),
    path('sent-notifications/' , ListBaseNotifications.as_view()),
    path('update-image/' , UpdateImage.as_view()),
    path('send-code/' , SendCodePassword.as_view()),
    path('verify-user/' , VerifyUser.as_view()),
    path('auth/reset-password/<str:user_id>/' , ResetPassword.as_view()),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view()),
    path('firebase-token/refresh/',RefreshFirebaseToken.as_view()),
    path('set-active/<str:user_id>/' , SetActive.as_view()),
    path('upload-audio/' , UploadAudio.as_view())
]


# Pilgrim app endpoints
PilgrimPatterns = [
    path('complete-step/<str:step_id>/' , CompleteStep.as_view()),
    path('prayers-timings/' , Calender.as_view()),
    path('register/' , RegisterPilgrim.as_view()),
    path('list-steps/' , ListHajSteps.as_view()),
    path('religious-categories/' , ListCreateReligiousCategory.as_view()),
    path('religious-category/<str:pk>/' , RetUpdDesReligiousCategory.as_view()),
    path('guidance-categories/' , ListCreateGuidanceCategory.as_view()),
    path('guidance-category/<str:pk>/' , RetUpdDesGuidanceCategory.as_view()),
    path('religious-posts/' , ListCreateReligiousPost.as_view()),
    path('religious-post/<str:pk>/' , RetUpdDesReligiousPost.as_view()),
    path('live-streams/' , ListLiveStream.as_view()),
    path('live-stream/<str:pk>/' , RetUpdDesLiveStream.as_view()),
    path('stream-types/' , ListCreateStreamType.as_view()),
    path('stream-type/<str:pk>/' , RetUpdDesStreamType.as_view()),
    path('guidance-posts/' , ListCreateGuidancePost.as_view()),
    path('guidance-post/<str:pk>/' , RetUpdDesGuidancePost.as_view()),
    path('get-guide/<str:pk>/' , GetGuide.as_view()),
    path('update-location/<str:pk>/' , UpdatePilgrimLocation.as_view())
]


# Manager app endpoints
ManagerPatterns = [
    path('list-manager-chats/' , ListManagerChats.as_view()),
    path('send-task/<str:pk>/' , SendTask.as_view()),
    path('list-chats/' , ListManagerChats.as_view()),
    path('get-chat/<str:pk>/' , GetChat.as_view()),
    path('send-notification/' , SendNotification.as_view()),
    path('list-pilgrims/' , ListPilgrim.as_view()),
    path('create-employee/' , CreateEmployee.as_view()),
    path('get-employee/<str:pk>/' , GetEmployee.as_view()),
    path('list-employees/' , ListEmployees.as_view()),
    path('update-employee/<str:pk>/' , UpdateEmployee.as_view()),
    path('get-pilgrim/<str:pk>/' , GetPilgrim.as_view()),
    path('get-note/<str:pk>/' , RetUpdDesNote.as_view()),
    path('delete-note/<str:pk>/' , RetUpdDesNote.as_view()),
    path('update-note/<str:pk>/' , RetUpdDesNote.as_view()),
    path('list-guides/' , ListGuides.as_view()),
    path('create-pilgrim/' , CreatePilgrim.as_view()),
    path('update-pilgrim/<str:pk>/' , UpdatePilgrim.as_view()),
    path('pilgrim-steps/<str:pilgrim_id>/' , PilgrimSteps.as_view()),
    path('delete-pilgrims' , DeletePilgrims.as_view()),
]


# Employee app endpoints
EmployeePatterns = [
    path('complete-task/<str:task_id>/' , CompleteTask.as_view()),
    path('accept-task/<str:task_id>/' , AcceptTask.as_view()),
    path('list-tasks/' , ListTask.as_view()),
    path('get-task/<str:pk>/' , RetUpdDesTask.as_view()),
]

# guide app endpoints
GuidePatterns = [
    path('create-note/' , CreateNote.as_view() , name="create-note"),
    path('list-notes/' , ListNote.as_view() , name="list-notes"),
    path('list-guide-chats/' , ListChats.as_view() , name="list-chats"),
    path('get-chat/<str:pk>/' , GetChat.as_view() , name="get-chat"),
    path('send-notification/' , SendNotification.as_view() , name="send-notification"),
    path('list-guide-pilgrims/' , ListGuidePilgrims.as_view() , name="list-guide-pilgrims"),
    path('get-pilgrim/<str:pk>/' , GetPilgrim.as_view() , name="get-pilgrim"),
    path('pilgrim-notes/<str:pk>/' ,  GetPilgrimNotes.as_view() , name="pilgrim-notes"),
    path('get-note/<str:pk>/' ,  RetUpdDesNote.as_view() , name="get-note"),
    path('delete-note/<str:pk>/' , RetUpdDesNote.as_view() , name="delete-note"),
    path('update-note/<str:pk>/' , RetUpdDesNote.as_view() , name="update-note")
]


urlpatterns = [
    path('' , include(AccountPatterns)),
    path('' , include(PilgrimPatterns)),
    path('' , include(ManagerPatterns)),
    path('' , include(EmployeePatterns)),
    path('' , include(GuidePatterns))
]
