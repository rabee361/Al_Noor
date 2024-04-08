from django.urls import path
from .views import *

urlpatterns = [
    path('prayers-timings/' , CalenderView.as_view() , name="prayers-timings")
]
