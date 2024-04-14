from typing import Any
from django.shortcuts import render
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

class PilgrimListView(TemplateView):
    template_name = 'users/customer/customer_list.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        pilgrims = Pilgrim.objects.all()
        context['pilgrims'] = pilgrims
        return context


class AddPilgrimView(TemplateView):
    template_name = 'users/customer/add_customer.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class UpdatePilgrimView(TemplateView):
    template_name = 'users/customer/update_customer.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class GuideListView(TemplateView):
    template_name = 'users/provider/provider_list.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        guides = Guide.objects.all()
        context['guides'] = guides
        return context


class AddGuideView(TemplateView):
    template_name = 'users/provider/add_provider.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

class UpdateGuideView(TemplateView):
    template_name = 'users/provider/update_provider.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

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
