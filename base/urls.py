from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('auth/login/' , LoginUserApiView.as_view() , name="login"),
    path('auth/logout/', LogoutUserAPIView.as_view(), name='logout'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('firebase-token/refresh/',RefreshFirebaseToken.as_view(),name="refresh-firebase-token"),
    path('prayers-timings/' , CalenderView.as_view() , name="prayers-timings"),
    path('list-notes/' , ListCreateNote.as_view() , name="list-notes"),
    path('get-note/' , RetUpdDesNote.as_view() , name="get-note"),
    # path('list-notifications/' , )
]
