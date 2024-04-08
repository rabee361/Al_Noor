from django.urls import path
from .views import *

urlpatterns = [
    path('prayers-timings/' , CalenderView.as_view() , name="prayers-timings"),
    path('list-notes/' , ListCreateNote.as_view() , name="list-notes"),
    path('get-note/' , RetUpdDesNote.as_view() , name="get-note"),
    # path('list-notifications/')
]
