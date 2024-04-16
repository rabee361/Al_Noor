import django_filters
from .models import *
  


class PilgrimFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='startswith')
    phonenumber = django_filters.CharFilter(field_name='user__phonenumber' , lookup_expr='startswith')

    class Meta:
        model = Pilgrim
        fields = ['name','phonenumber']



class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='user__username', lookup_expr='startswith')
    phonenumber = django_filters.CharFilter(field_name='user__phonenumber' , lookup_expr='startswith')
    
    class Meta:
        model = Employee
        fields = ['name','phonenumber']



class ManagementFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='user__username', lookup_expr='startswith')
    phonenumber = django_filters.CharFilter(field_name='user__phonenumber' , lookup_expr='startswith')
    
    class Meta:
        model = Management
        fields = ['name','phonenumber']



class GuideFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='user__username', lookup_expr='startswith')
    phonenumber = django_filters.CharFilter(field_name='user__phonenumber' , lookup_expr='startswith')
    
    class Meta:
        model = Guide
        fields = ['name','phonenumber']



class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter()

    class Meta:
        model = Task
        fields = ['completed']


class NoteFilter(django_filters.FilterSet):
    pilgrim_name = django_filters.CharFilter(field_name='pilgrim__user__username', lookup_expr='startswith')
    guide_name = django_filters.CharFilter(field_name='guide__user__username', lookup_expr='startswith')

    class Meta:
        model = Pilgrim
        fields = ['pilgrim_name','guide_name']