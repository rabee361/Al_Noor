from django.urls import path
from .views import *


urlpatterns = [
    path('test/' , TestView.as_view() , name="test"),
    path('' , mani_dashboard , name="main_dashboard"),

    path('login/' , login_user , name="login"),

    path('forms/' , registration_forms , name="registration_forms"),
    path('add_form/' , add_register_form , name="add_register_form"),
    path('delete_form/<str:form_id>' , delete_register_form , name="delete_register_form"),

    path('steps/' , steps , name="steps"),

    path('managers_list/' , managers_list , name="managers"),
    path('add_manager/' , add_manager , name="add_manager"),
    path('update_manager/<str:manager_id>/' , UpdateAdminView.as_view() , name="update_manager"),
    path('delete_manager/<str:manager_id>/' , delete_manager , name="delete_manager"),

    path('pilgrims_list/' , pilgrims_list , name="pilgrims"),
    path('add_pilgrim/' , add_pilgrim , name="add_pilgrim"),
    path('delete-pilgrim/<str:pilgrim_id>/' , delete_pilgrim , name="delete-pilgrim"),
    # path('update_pilgrim/<str:pk>/' , update_pilgrim, name="update_pilgrim"),

    path('guides_list/' , guides_list , name="guides"),
    path('add_guide/' , add_guide , name="add_guide"),
    path('update_guide/<str:pk>' , UpdateGuideView.as_view() , name="update_guide"),
    path('delete_guide/<str:pk>/' , delete_guide , name="delete_guide"),

    path('employees_list/' , employees_list , name="employees"),
    path('add_employee/' , add_employee , name="add_employee"),
    path('update_employee/<str:pk>' , UpdateGuideView.as_view() , name="update_employee"),
    path('delete_employee/<str:pk>/' , delete_employee , name="delete_employee"),

    path('tasks/' , task_list  , name="tasks"),
    path('add-task/' , add_task  , name="add_task"),
    path('delete-task/<str:task_id>/' , delete_task  , name="delete_task"),

    # path('guide_list/' , guides_list , name="guide_list"),
    # path('add_guide/' , AddGuideView.as_view() , name="add_guide"),
    # path('update_guide/<str:pk>/' , UpdateGuideView.as_view() , name="update_guide"),

    path('tasks/' , tasks , name="tasks"),
    path('notifications/' , notifications , name="notifications"),


    path('category_list/' , CategoryListView.as_view() , name="category_list"),
    path('main_service_list/' , MainServiceListView.as_view() , name="main_service_list"),
    path('subscription_list/' , SubscriptionListView.as_view() , name="subscription_list"),
    path('promotion-subscription-list/' ,  PromotionSubscriptionListView.as_view(), name="promotion-subscription-list"),
    path('login/' , LoginView.as_view() , name="login"),
    path('hi/' , HiView.as_view() , name="hi"),
    path('pilgrim/export', export_pilgram, name='export_pilgrim'),
    path('pilgrim/import', import_pilgrim, name='import_pilgrim'),
]
