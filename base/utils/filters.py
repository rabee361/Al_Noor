import django_filters
from ..models import *
from django.db.models import Q




class PilgrimFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='filter_query')

    class Meta:
        model = Pilgrim
        fields = ['query']

    def filter_query(self, queryset, name,value):
        if value:
            return queryset.filter(Q(phonenumber__icontains=value)|Q(first_name__istartswith=value))
        return queryset



class EmployeeFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='filter_query')
    
    class Meta:
        model = Employee
        fields = ['query']

    def filter_query(self, queryset, name,value):
        if value:
            return queryset.filter(Q(user__phonenumber__icontains=value)|Q(user__username__istartswith=value))
        return queryset



class ManagementFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='filter_query')

    class Meta:
        model = Management
        fields = ['query']

    def filter_query(self, queryset, name,value):
        if value:
            return queryset.filter(Q(user__phonenumber__icontains=value)|Q(user__username__istartswith=value))
        return queryset





class GuideFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='filter_query')

    class Meta:
        model = Guide
        fields = ['query']

    def filter_query(self, queryset, name,value):
        if value:
            return queryset.filter(Q(user__phonenumber__icontains=value)|Q(user__username__istartswith=value))
        return queryset



class TaskFilter(django_filters.FilterSet):
    completed = django_filters.BooleanFilter()
    accepted = django_filters.BooleanFilter()
    employee_name = django_filters.CharFilter(field_name='user__username' , lookup_expr='startswith')

    class Meta:
        model = Task
        fields = ['completed','accepted','employee_name']


class NoteFilter(django_filters.FilterSet):
    pilgrim_name = django_filters.CharFilter(field_name='pilgrim__user__username', lookup_expr='startswith')
    guide_name = django_filters.CharFilter(field_name='guide__user__username', lookup_expr='startswith')

    class Meta:
        model = Note
        fields = ['pilgrim_name','guide_name']



class GuidancePostFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(field_name='category__name' , lookup_expr='exact')
    
    class Meta:
        model = GuidancePost
        fields = ['category_name']




class ReligiousPostFilter(django_filters.FilterSet):
    category_name = django_filters.CharFilter(field_name='category__name' , lookup_expr='exact')

    class Meta:
        model = ReligiousPost
        fields = ['category_name']




class ChatFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method='filter_query')

    class Meta:
        model = Chat
        fields = ['query']

    def filter_query(self, queryset, name,value):
        if value:
            return queryset.filter(Q(user__phonenumber__icontains=value)|Q(user__username__istartswith=value))
        return queryset


