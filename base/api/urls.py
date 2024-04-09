from django.urls import path
from .views import *

urlpatterns = [
    path('create-pilgrim/' , CreatePilgrim.as_view()),
    path('list-create-religious-guide/<str:pk>/', ListCreateReligiousGuide.as_view()),
    path('get-upt-del-religious-guide/<str:pk>/', RetUptDelReligiousGuide.as_view()),
    path('list-create-religious-works/<str:pk>/', ListCreateReligiousWorks.as_view()),
    path('get-upt-del-religious-works/<str:pk>/', RetUptDelReligiousWorks.as_view()),
]
