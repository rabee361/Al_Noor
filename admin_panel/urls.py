from django.urls import path
from .views import *


urlpatterns = [
    path('' , mani_dashboard , name="main_dashboard"),

    path('login/' , login_user , name="login"),

    path('forms/' , registration_forms , name="registration_forms"),
    path('add_form/' , add_register_form , name="add_register_form"),
    path('delete_form/<str:form_id>' , delete_register_form , name="delete_register_form"),

    path('steps/' , steps , name="steps"),

    path('managers/' , managers_list , name="managers"),
    path('add_manager/' , add_manager , name="add_manager"),
    path('update_manager/<str:manager_id>/' , update_manager , name="update_manager"),
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
    path('update_employee/<str:employee_id>' , update_employee , name="update_employee"),
    path('delete_employee/<str:employee_id>/' , delete_employee , name="delete_employee"),

    path('tasks/' , task_list  , name="tasks"),
    path('add-task/' , add_task  , name="add_task"),
    path('update-task/<str:task_id>' , update_task  , name="update_task"),
    path('delete-task/<str:task_id>/' , delete_task  , name="delete_task"),

    # path('guide_list/' , guides_list , name="guide_list"),
    # path('add_guide/' , AddGuideView.as_view() , name="add_guide"),
    # path('update_guide/<str:pk>/' , UpdateGuideView.as_view() , name="update_guide"),

    path('notifications/' , notifications_list , name="notifications"),
    path('add-notification/' , add_notification , name="add_notification"),
    path('delete-notification/<str:notification_id>' , delete_notifications , name="delete_notification"),

    path('guidance-posts/' , guidance_posts , name="guidance_posts"),
    path('add-guidance-post/' , add_guidance_post , name="add_guidance_post"),
    path('update-guidance-post/<str:post_id>' , update_guidance_post , name="update_guidance_post"),
    path('delete-guidance-post/<str:post_id>' , delete_guidance_post , name="delete_guidance_post"),


    path('category_list/' , CategoryListView.as_view() , name="category_list"),
    path('main_service_list/' , MainServiceListView.as_view() , name="main_service_list"),
    path('subscription_list/' , SubscriptionListView.as_view() , name="subscription_list"),
    path('promotion-subscription-list/' ,  PromotionSubscriptionListView.as_view(), name="promotion-subscription-list"),
    path('pilgrim/import', import_pilgrim, name='import_pilgrim'),
    path('pilgrim/export', export_pilgram, name='export_pilgrim'),
    path('forms/export', export_forms, name='export_forms'),
    
]
