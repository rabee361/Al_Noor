from rest_framework.permissions import BasePermission
from ..models import *


class IsGuide(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        return Guide.objects.filter(user=user).exists()


class IsManager(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        return Management.objects.filter(user=user).exists()


class IsEmployee(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        return Employee.objects.filter(user=user).exists()


class IsPilgrim(BasePermission):
    def has_permission(self,request,view):
        user = request.user
        return Pilgrim.objects.filter(user=user).exists()