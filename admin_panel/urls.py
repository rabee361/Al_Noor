from django.urls import path
from .views import *


urlpatterns = [
    path('test/' , TestView.as_view() , name="test"),
    path('main_dashboard/' , MainDashboardView.as_view() , name="main_dashboard"),
    path('admin_list/' , AdminListView.as_view() , name="admin_list"),
    path('customer_list/' , CustomerListView.as_view() , name="customer_list"),
    path('provider_list/' , ProviderListView.as_view() , name="provider_list"),
    path('store_list/' , StoreListView.as_view() , name="store_list"),
    path('category_list/' , CategoryListView.as_view() , name="category_list"),
    path('main_service_list/' , MainServiceListView.as_view() , name="main_service_list"),
    path('subscription_list/' , SubscriptionListView.as_view() , name="subscription_list"),
    path('promotion-subscription-list/' ,  PromotionSubscriptionListView.as_view(), name="promotion-subscription-list"),
    path('login/' , LoginView.as_view() , name="login"),
    
]
