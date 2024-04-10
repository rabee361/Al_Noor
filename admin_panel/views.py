from django.shortcuts import render
from django.views.generic import TemplateView



class TestView(TemplateView):
    template_name = 'test.html'

class LoginView(TemplateView):
    template_name = 'login.html'

class MainDashboardView(TemplateView):
    template_name = 'main_dashboard.html'

class AdminListView(TemplateView):
    template_name = 'admin_list.html'

class CustomerListView(TemplateView):
    template_name = 'customer_list.html'

class ProviderListView(TemplateView):
    template_name = 'provider_list.html'

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
