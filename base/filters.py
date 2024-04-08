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


