from typing import Any
from django.shortcuts import render , HttpResponse
from django.views.generic import TemplateView
from base.models import *


class TestView(TemplateView):
    template_name = 'test.html'



class HiView(TemplateView):
    template_name = 'hi.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data['hi'] = 'hi'
        return context_data
    

class LoginView(TemplateView):
    template_name = 'login.html'

class MainDashboardView(TemplateView):
    template_name = 'main_dashboard.html'

class AdminListView(TemplateView):
    template_name = 'users/admin/admin_list.html'

class AddAdminView(TemplateView):
    template_name = 'users/admin/add_admin.html'

class UpdateAdminView(TemplateView):
    template_name = 'users/admin/update_admin.html'


def pilgrims_list(request):
    pilgrims = Pilgrim.objects.all()
    context = {
        'pilgrims':pilgrims
    }
    return render(request , 'users/customer/pligrims_list.html' , context)


class AddPilgrimView(TemplateView):
    template_name = 'users/customer/add_pilgrim.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class UpdatePilgrimView(TemplateView):
    template_name = 'users/customer/update_pilgrim.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


def delete_pilgrim(request,pilgrim_id):
    Pilgrim.objects.get(id=pilgrim_id).delete()
    return HttpResponse("greate")





def managers_list(request):
    managers = Management.objects.all()
    context = {
        'managers':managers
    }
    return render(request , 'users/admin/managers_list.html' , context)


class AddPilgrimView(TemplateView):
    template_name = 'users/customer/add_pilgrim.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class UpdatePilgrimView(TemplateView):
    template_name = 'users/customer/update_pilgrim.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


def delete_manager(request,manager_id):
    Management.objects.get(id=manager_id).delete()
    return HttpResponse("greate")






def guides_list(request):
    guides = Guide.objects.all()
    context = {
        'guides':guides
    }
    return render(request , 'users/provider/guides_list.html' , context)


class AddGuideView(TemplateView):
    template_name = 'users/provider/add_guide.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

class UpdateGuideView(TemplateView):
    template_name = 'users/provider/update_guide.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

def delete_guide(self,request,guide_id):
    Guide.objects.get(id=guide_id).delete()
    return HttpResponse("great")


def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees
    }
    return render(request , 'users/employee/employees_list.html' , context)


class AddGuideView(TemplateView):
    template_name = 'users/provider/add_guide.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

class UpdateGuideView(TemplateView):
    template_name = 'users/provider/update_guide.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

def delete_guide(self,request,guide_id):
    Guide.objects.get(id=guide_id).delete()
    return HttpResponse("great")


class StoreListView(TemplateView):
    template_name = 'store_list.html'

class CategoryListView(TemplateView):
    template_name = 'category_list.html'

class MainServiceListView(TemplateView):
    template_name = 'main_service_list.html'

class SubscriptionListView(TemplateView):
    template_name = 'subscription_list.html'

class PromotionSubscriptionListView(TemplateView):
    template_name = 'promotion-subscription-list.html'
