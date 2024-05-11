from typing import Any
from django.shortcuts import render , HttpResponse , redirect
from django.views.generic import TemplateView
from base.models import *
from base.resources import PilgrimResource , RegistrationResource
from .forms import *
from .forms import PilgrimForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
import pandas as pd
from django.core.files.storage import default_storage
from django.db import transaction
from django.views import View




def login_user(request):
    if request.method == 'POST':
        phonenumber = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=phonenumber, password=password)
        if user is not None:
            login(request,user)
            return redirect('main_dashboard')

    return render(request , 'login.html')




def logout_user(request):
    logout(request)
    return redirect('login')




@login_required(login_url='login')
def main_dashboard(request):
    total_pilgrims = Pilgrim.objects.count()
    total_employees = Employee.objects.count()
    total_managers = Management.objects.count()
    total_guides = Guide.objects.count()
    total_forms = Registration.objects.count()
    user_image = request.user.image.url
    username = request.user.username
    context = {
    'total_pilgrims' : total_pilgrims,
    'total_employees' : total_employees,
    'total_managers' : total_managers,
    'total_guides' : total_guides,
    'total_forms' : total_forms,
    'user_image' : user_image,
    'username' : username
    }
    return render(request , 'dashboard.html' , context)



@login_required(login_url='login')
def registration_forms(request):
    context = {

    }
    return render(request , 'registration_forms.html' , context=context)



@login_required(login_url='login')
def steps(request):
    context = {

    }
    return render(request , 'steps.html' , context=context)


@login_required(login_url='login')
def registration_forms(request):
    q = request.GET.get('q') or ''
    print(q)
    forms = Registration.objects.filter(first_name__startswith = q).order_by('-id')
    user_image = request.user.image.url
    username = request.user.username

    context = {
        'forms':forms,
        'user_image' : user_image,
        'username' : username
 }
    return render(request , 'registration_forms.html' , context)





@login_required(login_url='login')
def add_register_form(request):
    form = NewRegisterForm()
    user_image = request.user.image.url
    username = request.user.username

    if request.method == 'POST':
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_forms')

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_form.html', context)





@login_required(login_url='login')
def update_register_form(request,form_id):
    register_form = Registration.objects.get(id=form_id)
    form = NewRegisterForm(instance=register_form)
    user_image = request.user.image.url
    username = request.user.username

    if request.method == 'POST':
        form = NewRegisterForm(request.POST,instance=register_form)
        if form.is_valid():
            form.save()
            return redirect('registration_forms')

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_form.html', context)






def delete_register_form(request,form_id):
    Registration.objects.get(id=form_id).delete()

    return redirect('registration_forms')








@login_required(login_url='login')
def pilgrims_list(request):
    q = request.GET.get('q') or ''
    print(q)
    pilgrims = Pilgrim.objects.filter(first_name__startswith = q).order_by('-id')
    user_image = request.user.image.url
    username = request.user.username
    context = {
        'pilgrims':pilgrims,
        'user_image' : user_image,
        'username' : username
 }
    return render(request , 'pilgrims_list.html' , context)





class update_pilgrim(View):
    def get(self, request,pilgrim_id):
        pilgrim = Pilgrim.objects.get(id=pilgrim_id)
        user = CustomUser.objects.get(id=pilgrim.user.id)
        user_form = CustomUserCreationForm(instance=user)
        form = PilgrimForm(instance=pilgrim)
        context = {'user_form': user_form,
                    'form': form,
                    
                    }
        return render(request, 'update_pilgrim.html', context=context)

    def post(self, request, *args, **kwargs):
        user_form = CustomUserCreationForm(request.POST)
        pilgrim_form = PilgrimForm(request.POST, request.FILES)
        if user_form.is_valid() and pilgrim_form.is_valid():
            user = user_form.save()
            pilgrim = pilgrim_form.save(commit=False)
            pilgrim.user = user
            pilgrim.save()
            return redirect('pilgrims')  # Redirect to a success page
        return render(request, 'registration/pilgrim_registration.html', {'user_form': user_form, 'pilgrim_form': pilgrim_form})







@login_required(login_url='login')
def add_pilgrim(request):
    form = NewPilgrim()
    user_image = request.user.image.url
    username = request.user.username

    if request.method == 'POST':
        form = NewPilgrim(request.POST, request.FILES)  # Ensure you pass request.FILES if you're handling files
        print(form.is_valid())
        if form.is_valid():
            user = CustomUser.objects.create(
                username=form.cleaned_data['first_name'],
                phonenumber=form.cleaned_data['phonenumber'],
                # email=form.cleaned_data['email'],
                password=form.cleaned_data['password'],
                get_notifications=form.cleaned_data['get_notifications'],
                image=form.cleaned_data['image'],
            )

            print(user)
            pilgrim = Pilgrim.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                father_name=form.cleaned_data['father_name'],
                last_name=form.cleaned_data['last_name'],
                grand_father=form.cleaned_data['grand_father'],
                phonenumber=form.cleaned_data['phonenumber'],
                hotel=form.cleaned_data['hotel'],
                hotel_address=form.cleaned_data['hotel_address'],
                birthday=form.cleaned_data['birthday'],
                duration=form.cleaned_data['duration'],
                borading_time=form.cleaned_data['borading_time'],
                gate_num=form.cleaned_data['gate_num'],
                arrival=form.cleaned_data['arrival'],
            )

            return redirect('pilgrims')
        
        else:
            return redirect('pilgrims')
    

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_pilgrim.html', context)






# @login_required(login_url='login')
# def update_pilgrim(request,pilgrim_id):
#     pilgrim = Pilgrim.objects.get(id=pilgrim_id)
#     user = CustomUser.objects.get(id=pilgrim.user)
#     form = UpdatePilgrim(instance=user)

#     if request.method == 'POST':
#         form = UpdatePilgrim(request.POST,request.FILES,instance=pilgrim)
#         if form.is_valid():
#             user = CustomUser.objects.get(
#                 phonenumber=form.cleaned_data['phonenumber'],
#             )
#             password1=form.cleaned_data['password1']
#             password2=form.cleaned_data['password2']
#             image=request.FILES.get('image')
#             print(image)
#             if image:
#                 user.image = request.FILES.get('image')
#             else:
#                 user.image = pilgrim.user.image
#             # if password1:
#             #     user.set_password(password1)


#             user.get_notifications = form.cleaned_data['get_notifications']
#             user.username = form.cleaned_data['username']
#             user.save()
#             return redirect('pilgrims')

#     user_image = request.user.image.url
#     pilgrim_image = pilgrim.user.image.url
#     username = request.user.username
    
#     context = {
#         'form': form,
#         'user_image': user_image,
#         'pilgrim_image': pilgrim_image,
#         'username': username,
#     }
#     return render(request, 'update_pilgrim.html', context)





@login_required(login_url='login')
def delete_pilgrim(request,pk):
    Pilgrim.objects.get(id=pk).delete()

    return redirect('pilgrims-list')






@login_required(login_url='login')
def managers_list(request):
    q = request.GET.get('q') or ''
    user_image = request.user.image.url
    username = request.user.username
    managers = Management.objects.filter(user__first_name__startswith = q).order_by('-id')
    context = {
        'managers':managers,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'managers_list.html' , context)








@login_required(login_url='login')
def add_manager(request):
    form = NewManager()
    user_image = request.user.image.url
    username = request.user.username
    if request.method == 'POST':
        form = NewManager(request.POST, request.FILES)
        if form.is_valid():
            user = CustomUser.objects.create(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                # email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                get_notifications=form.cleaned_data['get_notifications'],
                image=form.cleaned_data['image'],
            )
            
            Management.objects.create(user=user)
            return redirect('managers')
    context = {
        'form' : form,
        'user_image': user_image,
        'username': username,
    }
    return render(request , 'add_manager.html' , context)







@login_required(login_url='login')
def update_manager(request,manager_id):
    manager = Management.objects.get(id=manager_id)
    user = manager.user
    form = UpdateManager(instance=user)

    if request.method == 'POST':
        form = UpdateManager(request.POST,request.FILES,instance=manager)
        if form.is_valid():
            user = CustomUser.objects.get(
                phonenumber=form.cleaned_data['phonenumber'],
            )
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            image=request.FILES.get('image')
            print(image)
            if image:
                user.image = request.FILES.get('image')
            else:
                user.image = manager.user.image
            # if password1:
            #     user.set_password(password1)


            user.get_notifications = form.cleaned_data['get_notifications']
            user.username = form.cleaned_data['username']
            user.save()
            return redirect('managers')

    user_image = request.user.image.url
    manager_image = manager.user.image.url
    username = request.user.username
    
    context = {
        'form': form,
        'user_image': user_image,
        'manager_image': manager_image,
        'username': username,
    }
    return render(request, 'update_manager.html', context)




@login_required(login_url='login')
def delete_manager(request,manager_id):
    Management.objects.get(id=manager_id).delete()
    return HttpResponse("greate")










@login_required(login_url='login')
def task_list(request):
    q = request.GET.get('q') or ''
    tasks = Task.objects.filter(title__startswith = q).order_by('-id')
    user_image = request.user.image.url
    username = request.user.username
    context = {
        'tasks':tasks,
        'user_image' : user_image,
        'username' : username
 }
    return render(request , 'tasks.html' , context)








@login_required(login_url='login')
def add_task(request):
    form = NewTask()
    user_image = request.user.image.url
    username = request.user.username

    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_task.html', context)







@login_required(login_url='login')
def update_task(request,task_id):
    task = Task.objects.get(id=task_id)
    form = NewTask(instance=task)
    user_image = request.user.image.url
    username = request.user.username

    if request.method == 'POST':
        form = NewTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_task.html', context)







@login_required(login_url='login')
def delete_task(request,task_id):
    Task.objects.get(id=task_id).delete()

    return redirect('tasks')















@login_required(login_url='login')
def employees_list(request):
    q = request.GET.get('q') or ''
    user_image = request.user.image.url
    username = request.user.username
    employees = Employee.objects.filter(user__username__startswith=q).order_by('-id')
    context = {
        'employees':employees,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'employees_list.html' , context)



@login_required(login_url='login')
def add_employee(request):
    form = NewEmployee()
    user_image = request.user.image.url
    username = request.user.username
    if request.method == 'POST':
        form = NewEmployee(request.POST, request.FILES)
        if form.is_valid():
            user = CustomUser.objects.create(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                # email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                get_notifications=form.cleaned_data['get_notifications'],
                image=form.cleaned_data['image'],
            )
            
            Employee.objects.create(user=user)
            return redirect('employees')
    context = {
        'form' : form,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'add_employee.html' , context)

    



@login_required(login_url='login')
def update_employee(request,employee_id):
    employee = Employee.objects.get(id=employee_id)
    user = employee.user
    form = UpdateEmployee(instance=user)

    if request.method == 'POST':
        form = UpdateEmployee(request.POST,request.FILES,instance=employee)
        if form.is_valid():
            user = CustomUser.objects.get(
                phonenumber=form.cleaned_data['phonenumber'],
            )
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            image=request.FILES.get('image')
            print(image)
            if image:
                user.image = request.FILES.get('image')
            else:
                user.image = employee.user.image
            # if password1:
            #     user.set_password(password1)


            user.get_notifications = form.cleaned_data['get_notifications']
            user.username = form.cleaned_data['username']
            user.save()
            return redirect('employees')

    user_image = request.user.image.url
    employee_image = employee.user.image.url
    username = request.user.username
    
    context = {
        'form': form,
        'user_image': user_image,
        'employee_image': employee_image,
        'username': username,
    }
    return render(request, 'update_employee.html', context)








@login_required(login_url='login')
def delete_employee(request,employee_id):
    Employee.objects.get(id=employee_id).delete()
    return redirect('employees')






@login_required(login_url='login')
def guides_list(request):
    q = request.GET.get('q') or ''
    user_image = request.user.image.url
    username = request.user.username
    guides = Guide.objects.filter(user__username__startswith=q).order_by('-id')
    context = {
        'guides':guides,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'guides_list.html' , context)



@login_required(login_url='login')
def add_guide(request):
    form = NewGuide()
    user_image = request.user.image.url
    username = request.user.username
    if request.method == 'POST':
        form = NewGuide(request.POST, request.FILES)
        if form.is_valid():
            user = CustomUser.objects.create(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                # email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                get_notifications=form.cleaned_data['get_notifications'],
                image=form.cleaned_data['image'],
            )
            
            Employee.objects.create(user=user)
            return redirect('guides')
    context = {
        'form' : form,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'add_guide.html' , context)





def update_guide(request,guide_id):
    guide = Guide.objects.get(id=guide_id)
    user = guide.user
    form = UpdateGuide(instance=user)

    if request.method == 'POST':
        form = UpdateGuide(request.POST,request.FILES,instance=guide)
        if form.is_valid():
            user = CustomUser.objects.get(
                phonenumber=form.cleaned_data['phonenumber'],
            )
            password1=form.cleaned_data['password1']
            password2=form.cleaned_data['password2']
            image=request.FILES.get('image')
            print(image)
            if image:
                user.image = request.FILES.get('image')
            else:
                user.image = guide.user.image
            # if password1:
            #     user.set_password(password1)


            user.get_notifications = form.cleaned_data['get_notifications']
            user.username = form.cleaned_data['username']
            user.save()
            return redirect('guides')

    user_image = request.user.image.url
    guide_image = guide.user.image.url
    username = request.user.username
    
    context = {
        'form': form,
        'user_image': user_image,
        'guide_image': guide_image,
        'username': username,
    }
    return render(request, 'update_guide.html', context)


    

def delete_guide(request,guide_id):
    Guide.objects.get(id=guide_id).delete()
    return redirect('guides')









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

class DashboardView(TemplateView):
    template_name = 'base.html'

class PromotionSubscriptionListView(TemplateView):
    template_name = 'promotion-subscription-list.html'

class PromotionSubscriptionListView(TemplateView):
    template_name = 'promotion-subscription-list.html'


def export_pilgram(request):
    pilgrim_resource = PilgrimResource()
    dataset = pilgrim_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="pilgrims.xlsx"'
    return response



def export_forms(request):
    pilgrim_resource = RegistrationResource()
    dataset = pilgrim_resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="register_forms.xlsx"'
    return response



@transaction.atomic
def import_pilgrim(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        # file_path = default_storage.save('temp/' + excel_file.name, excel_file)
        df = pd.read_excel(excel_file)  # or 'xlrd' for.xls files

        # df['وقت الصعود'] = pd.to_datetime(df['وقت الصعود'], format='%H:%M', errors='coerce')
        # df['تاريخ الميلاد'] = pd.to_datetime(df['تاريخ الميلاد - الميلادي فقط'], errors='coerce')

        # Assuming the Excel file has columns that match the Pilgrim model fields
        for index, row in df.iterrows():
            # Convert phone number to a PhoneNumber object
            user =CustomUser.objects.create(phonenumber=str(row['رقم الجوال']) , username=str(row['الاسم الأول']) )
            user.save()
            # Create a Pilgrim object
            pilgrim = Pilgrim(
                user=user,  # You need to set this based on your application logic
                registeration_id=row['رقم الهوية'],
                first_name=row['الاسم الأول'],
                father_name=row['اسم الأب'],
                grand_father=row['اسم الجد'],
                last_name=row['العائلة'],
                # birthday=row['تاريخ الميلاد - الميلادي فقط'],
                phonenumber=str(row['رقم الجوال']),
                # flight_num=row['رقم الرحلة'],
                # arrival=row['arrival'],
                # departure=row['departure'],
                duration=row['مدة الرحلة'],
                # borading_time=row['وقت الصعود'],
                gate_num=row['رقم البوابة'],
                flight_company=row['شركة الطيران'],
                # company_logo=row['شعار الشركة'],  # This needs to be handled as an ImageFile
                status=True,
                hotel=row['الفندق'],
                hotel_address=row['عنوان الفندق'],
                room_num=33,
                # haj_steps=row['haj_steps'],  # This needs to be handled as a ManyToManyField
                # created=row['created']
            )
            pilgrim.save()

        return render(request, 'pilgrims_list.html', {'message': 'Data imported successfully'})
    return render(request, 'user.html')


def notifications_list(request):
    q = request.GET.get('q') or ''
    user_image = request.user.image.url
    username = request.user.username
    notifications = BaseNotification.objects.filter(title__startswith=q).order_by('-id')
    context = {
        'notifications':notifications,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'notifications_list.html' , context)







@login_required(login_url='login')
def add_notification(request):
    form = NotificationForm()
    user_image = request.user.image.url
    username = request.user.username
    if request.method == 'POST':
        form = NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('notifications')
    context = {
        'form' : form,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'add_notification.html' , context)

    


def delete_notifications(request,notification_id):
    BaseNotification.objects.get(id=notification_id).delete()
    return redirect('notifications')







def guidance_posts(request):
    q = request.GET.get('q') or ''
    user_image = request.user.image.url
    username = request.user.username
    posts = GuidancePost.objects.filter(title__startswith=q).order_by('-id')
    context = {
        'posts':posts,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'guidance_posts.html' , context)






@login_required(login_url='login')
def add_guidance_post(request):
    form = GuidancePostForm()
    user_image = request.user.image.url
    username = request.user.username
    if request.method == 'POST':
        form = GuidancePostForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('guidance_posts')
    context = {
        'form' : form,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'add_guidance_post.html' , context)





@login_required(login_url='login')
def update_guidance_post(request,post_id):
    post = GuidancePost.objects.get(id=post_id)
    form = GuidancePostForm(instance=post)
    user_image = request.user.image.url
    username = request.user.username

    if request.method == 'POST':
        form = GuidancePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('guidance_posts')

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_guidance_post.html', context)





@login_required(login_url='login')
def delete_guidance_post(request,post_id):
    GuidancePost.objects.get(id=post_id).delete()
    return redirect('guideance_posts')





@login_required(login_url='login')
def steps_list(request):
    q = request.GET.get('q') or ''
    user_image = request.user.image.url
    username = request.user.username
    steps = HajSteps.objects.filter(name__startswith=q).order_by('-id')
    context = {
        'steps':steps,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'steps.html' , context)






@login_required(login_url='login')
def add_step(request):
    form = StepForm()
    user_image = request.user.image.url
    username = request.user.username
    if request.method == 'POST':
        form = StepForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('steps')
    context = {
        'form' : form,
        'user_image': user_image,
        'username': username
    }
    return render(request , 'add_step.html' , context)





@login_required(login_url='login')
def update_step(request,step_id):
    step = HajSteps.objects.get(id=step_id)
    form = StepForm(instance=step)
    user_image = request.user.image.url
    username = request.user.username

    if request.method == 'POST':
        form = StepForm(request.POST, instance=step)
        if form.is_valid():
            form.save()
            return redirect('steps')

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_step.html', context)





@login_required(login_url='login')
def delete_step(request,step_id):
    HajSteps.objects.get(id=step_id).delete()
    return redirect('steps')

