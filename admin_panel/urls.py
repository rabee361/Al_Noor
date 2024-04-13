from django.urls import path
from .views import *


urlpatterns = [
    path('test/' , TestView.as_view() , name="test"),
    path('main_dashboard/' , MainDashboardView.as_view() , name="main_dashboard"),
    path('admin_list/' , AdminListView.as_view() , name="admin_list"),
    path('add_admin/' , AddAdminView.as_view() , name="add_admin"),
    path('update_admin/' , UpdateAdminView.as_view() , name="update_admin"),
    path('customer_list/' , CustomerListView.as_view() , name="customer_list"),
    path('add_customer/' , AddCustomerView.as_view() , name="add_customer"),
    path('update_customer/' , UpdateCustomerView.as_view() , name="update_customer"),
    path('provider_list/' , ProviderListView.as_view() , name="provider_list"),
    path('add_provider/' , AddProviderView.as_view() , name="add_provider"),
    path('update_provider/' , UpdateProviderView.as_view() , name="update_provider"),
    path('store_list/' , StoreListView.as_view() , name="store_list"),
    path('category_list/' , CategoryListView.as_view() , name="category_list"),
    path('main_service_list/' , MainServiceListView.as_view() , name="main_service_list"),
    path('subscription_list/' , SubscriptionListView.as_view() , name="subscription_list"),
    path('promotion-subscription-list/' ,  PromotionSubscriptionListView.as_view(), name="promotion-subscription-list"),
    path('login/' , LoginView.as_view() , name="login"),
    path('hi/' , HiView.as_view() , name="hi"),
    
]
