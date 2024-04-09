from django.urls import path
from .views import *

urlpatterns = [
    path('create-pilgrim/' , CreatePilgrim.as_view()),
]
