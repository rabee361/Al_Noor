from django.urls import path
from .views import *


urlpatterns = [
    path('' , main_dashboard , name="main_dashboard"),
 
    path('my-account/' , my_account , name="my_account"),
    path('add-admin/' , add_admin , name="add_admin"),
    path('admins/' , admins_list , name="admins"),
    path('admins/update/<str:admin_id>' , update_admin , name="update_admin"),
    path('admin/delete/<str:admin_id>' , delete_admin , name="delete_admin"),

    path('login/' , login_user , name="login"),
    path('logout/' , logout_user , name="logout"),
    path('change-password/<str:user_id>/' , change_password , name="change_password"),

    path('forms/' , registration_forms , name="registration_forms"),
    path('forms/add' , add_register_form , name="add_register_form"),
    path('forms/update/<str:form_id>' , update_register_form , name="update_register_form"),
    path('forms/delete/<str:form_id>' , delete_register_form , name="delete_register_form"),
    path('delete-all-forms/' , delete_all_forms , name="delete_all_forms"),
    path('forms/export', export_forms, name='export_forms'),

    path('managers/' , managers_list , name="managers"),
    path('manager/add' , add_manager , name="add_manager"),
    path('managers/update/<str:manager_id>' , update_manager , name="update_manager"),
    path('managers/delete/<str:manager_id>' , delete_manager , name="delete_manager"),

    path('pilgrims/' , pilgrims_list , name="pilgrims"),
    path('pilgrims/add' , AddPilgrimView.as_view() , name="add_pilgrim"),
    path('pilgrims/update/<str:pilgrim_id>' , update_pilgrim, name="update_pilgrim"),
    path('pilgrims/delete/<str:pilgrim_id>' , delete_pilgrim , name="delete_pilgrim"),
    path('delete-all-pilgrims/' , delete_all_pilgrims , name="delete_all_pilgrims"),
    path('pilgrim/import', import_pilgrim, name='import_pilgrim'),
    path('pilgrim/export', export_pilgram, name='export_pilgrim'),

    path('guides/' , guides_list , name="guides"),
    path('guides/add' , add_guide , name="add_guide"),
    path('guides/update/<str:guide_id>' , update_guide , name="update_guide"),
    path('guides/delete/<str:guide_id>/' , delete_guide , name="delete_guide"),

    path('employees/' , employees_list , name="employees"),
    path('employees/add' , add_employee , name="add_employee"),
    path('employees/update/<str:employee_id>' , update_employee , name="update_employee"),
    path('employees/delete/<str:employee_id>' , delete_employee , name="delete_employee"),

    path('tasks/' , task_list  , name="tasks"),
    path('tasks/add' , add_task  , name="add_task"),
    path('tasks/update/<str:task_id>' , update_task  , name="update_task"),
    path('tasks/delete/<str:task_id>' , delete_task  , name="delete_task"),
   
    path('notes/' , notes_list  , name="notes"),
    path('notes/add' , add_note  , name="add_note"),
    path('notes/update/<str:note_id>' , update_note  , name="update_note"),
    path('notes/delete/<str:note_id>' , delete_note  , name="delete_note"),

    path('notifications/' , notifications_list , name="notifications"),
    path('notifications/add' , add_notification , name="add_notification"),
    path('notifications/delete/<str:notification_id>' , delete_notifications , name="delete_notification"),

    path('guidance-posts/' , guidance_posts , name="guidance_posts"),
    path('guidance-posts/add' , add_guidance_post , name="add_guidance_post"),
    path('guidance-posts/update/<str:post_id>' , update_guidance_post , name="update_guidance_post"),
    path('guidance-posts/delete/<str:post_id>' , delete_guidance_post , name="delete_guidance_post"),

    path('guidance-categories/' , guidance_categories , name="guidance_categories"),
    path('guidance-categories/add' , add_guidance_category , name="add_guidance_category"),
    path('guidance-categories/update/<str:category_id>' , update_guidance_category , name="update_guidance_category"),
    path('guidance-categories/delete/<str:category_id>' , delete_guidance_category , name="delete_guidance_category"),
    
    path('religious-posts/' , religious_posts , name="religious_posts"),
    path('religious-posts/add' , add_religious_post , name="add_religious_post"),
    path('religious-posts/update/<str:post_id>' , update_religious_post , name="update_religious_post"),
    path('religious-posts/delete/<str:post_id>' , delete_religious_post , name="delete_religious_post"),

    path('religious-categories/' , religious_categories , name="religious_categories"),
    path('religious-categories/add' , add_religious_category , name="add_religious_category"),
    path('religious-categories/update/<str:category_id>' , update_religious_category , name="update_religious_category"),
    path('religious-categories/delete/<str:category_id>' , delete_religious_category , name="delete_religious_category"),
    
    path('stream-types/' , stream_types , name="stream_types"),
    path('stream-types/add/' , add_stream_type , name="add_stream_type"),
    path('stream-types/update/<str:id>/' , update_stream_type , name="update_stream_type"),
    path('stream-types/delete/<str:id>/' , delete_stream_type , name="delete_stream_type"),
    
    path('live-streams/' , live_streams , name="live_streams"),
    path('live-streams/add/' , add_live_stream , name="add_live_stream"),
    path('live-streams/update/<str:id>/' , update_live_stream , name="update_live_stream"),
    path('live-streams/delete/<str:id>/' , delete_live_stream , name="delete_live_stream"),

    path('steps/' , steps_list , name="steps"),
    path('pilgrim-steps/' , pilgrim_steps , name="pilgrim_steps"),
    path('steps/add' , add_step , name="add_step"),
    path('steps/update/<str:step_id>' , update_step , name="update_step"),
    path('steps/delete/<str:step_id>' , delete_step , name="delete_step"),
    
    path('secondary-steps/' , secondary_steps_list , name="secondary_steps"),
    path('secondary-steps/add' , add_secondary_step , name="add_secondary_step"),
    path('secondary-steps/update/<str:step_id>' , update_secondary_step , name="update_secondary_step"),
    path('secondary-steps/delete/<str:step_id>' , delete_secondary_step , name="delete_secondary_step"),

    path('terms_privacy/' , terms , name="terms"),
    path('terms_privacy/update/' , update_terms , name="update_terms"),

]
