from rest_framework.views import APIView
from .permissions import AccountExists
from rest_framework.permissions import IsAuthenticated



class BaseAPIView(APIView):
    permission_classes = [IsAuthenticated]