from django.urls import path
from .views import *


urlpatterns = [
    path('' , main_dashboard , name="main_dashboard"),
 
    path('my-account/' , my_account , name="my_account"),
    path('add-admin/' , add_admin , name="add_admin"),
    path('admins/' , admins_list , name="admins"),
    path('update-admin/<str:admin_id>' , update_admin , name="update_admin"),
    path('delete-admin/<str:admin_id>' , delete_admin , name="delete_admin"),

    path('login/' , login_user , name="login"),
    path('logout/' , logout_user , name="logout"),
    path('change-password/<str:user_id>/' , change_password , name="change_password"),

    path('forms/' , registration_forms , name="registration_forms"),
    path('add_form/' , add_register_form , name="add_register_form"),
    path('update_form/<str:form_id>' , update_register_form , name="update_register_form"),
    path('delete_form/<str:form_id>' , delete_register_form , name="delete_register_form"),
    path('delete-all-forms/' , delete_all_forms , name="delete_all_forms"),

    path('managers/' , managers_list , name="managers"),
    path('add_manager/' , add_manager , name="add_manager"),
    path('update_manager/<str:manager_id>/' , update_manager , name="update_manager"),
    path('delete_manager/<str:manager_id>/' , delete_manager , name="delete_manager"),

    path('pilgrims_list/' , pilgrims_list , name="pilgrims"),
    path('add_pilgrim/' , AddPilgrimView.as_view() , name="add_pilgrim"),
    path('update_pilgrim/<str:pilgrim_id>/' , update_pilgrim, name="update_pilgrim"),
    path('delete-pilgrim/<str:pilgrim_id>/' , delete_pilgrim , name="delete-pilgrim"),
    path('delete-all-pilgrims/' , delete_all_pilgrims , name="delete_all_pilgrims"),

    path('guides_list/' , guides_list , name="guides"),
    path('add_guide/' , add_guide , name="add_guide"),
    path('update_guide/<str:guide_id>' , update_guide , name="update_guide"),
    path('delete_guide/<str:guide_id>/' , delete_guide , name="delete_guide"),

    path('employees_list/' , employees_list , name="employees"),
    path('add_employee/' , add_employee , name="add_employee"),
    path('update_employee/<str:employee_id>' , update_employee , name="update_employee"),
    path('delete_employee/<str:employee_id>/' , delete_employee , name="delete_employee"),

    path('tasks/' , task_list  , name="tasks"),
    path('add-task/' , add_task  , name="add_task"),
    path('update-task/<str:task_id>' , update_task  , name="update_task"),
    path('delete-task/<str:task_id>/' , delete_task  , name="delete_task"),
   
    path('notes/' , notes_list  , name="notes"),
    path('add-note/' , add_note  , name="add_note"),
    path('update-note/<str:note_id>/' , update_note  , name="update_note"),
    path('delete-note/<str:note_id>/' , delete_note  , name="delete_note"),

    path('notifications/' , notifications_list , name="notifications"),
    path('add-notification/' , add_notification , name="add_notification"),
    path('delete-notification/<str:notification_id>' , delete_notifications , name="delete_notification"),

    path('guidance-posts/' , guidance_posts , name="guidance_posts"),
    path('add-guidance-post/' , add_guidance_post , name="add_guidance_post"),
    path('update-guidance-post/<str:post_id>/' , update_guidance_post , name="update_guidance_post"),
    path('delete-guidance-post/<str:post_id>/' , delete_guidance_post , name="delete_guidance_post"),

    path('guidance-categories/' , guidance_categories , name="guidance_categories"),
    path('add-guidance-category/' , add_guidance_category , name="add_guidance_category"),
    path('update-guidance-category/<str:category_id>' , update_guidance_category , name="update_guidance_category"),
    path('delete-guidance-category/<str:category_id>' , delete_guidance_category , name="delete_guidance_category"),
    
    path('religious-posts/' , religious_posts , name="religious_posts"),
    path('add-religious-post/' , add_religious_post , name="add_religious_post"),
    path('update-religious-post/<str:post_id>/' , update_religious_post , name="update_religious_post"),
    path('delete-religious-post/<str:post_id>/' , delete_religious_post , name="delete_religious_post"),

    path('religious-categories/' , religious_categories , name="religious_categories"),
    path('add-religious-category/' , add_religious_category , name="add_religious_category"),
    path('update-religious-category/<str:category_id>' , update_religious_category , name="update_religious_category"),
    path('delete-religious-category/<str:category_id>' , delete_religious_category , name="delete_religious_category"),
    
    path('steps/' , steps_list , name="steps"),
    path('pilgrim-steps/' , pilgrim_steps , name="pilgrim_steps"),
    path('add-step/' , add_step , name="add_step"),
    path('update-step/<str:step_id>' , update_step , name="update_step"),
    path('delete-step/<str:step_id>' , delete_step , name="delete_step"),
    
    path('secondary-steps/' , secondary_steps_list , name="secondary_steps"),
    path('add-secondary-step/' , add_secondary_step , name="add_secondary_step"),
    path('update-secondary-step/<str:step_id>' , update_secondary_step , name="update_secondary_step"),
    path('delete-secondary-step/<str:step_id>' , delete_secondary_step , name="delete_secondary_step"),

    path('pilgrim/import', import_pilgrim, name='import_pilgrim'),
    path('pilgrim/export', export_pilgram, name='export_pilgrim'),
    path('forms/export', export_forms, name='export_forms'),

    path('terms_privacy/' , terms , name="terms"),
    path('update_terms/' , update_terms , name="update_terms"),

]
