from typing import Any
from django.shortcuts import render , HttpResponse , redirect
from django.views.generic import TemplateView
from base.models import *
from base.resources import PilgrimResource , RegistrationResource
from .forms import *
from import_export.admin import ImportExportModelAdmin
from .forms import PilgrimForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout






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
def mani_dashboard(request):
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
                gate_num=form.cleaned_data['gate_num'],
                arrival=form.cleaned_data['arrival'],
            )

            return redirect('pilgrims')
        
        else:
            print(form.errors)
            return redirect('pilgrims')
    

    context = {
        'form': form,
        'user_image': user_image,
        'username': username
    }
    return render(request, 'add_pilgrim.html', context)




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
        'form' : form
    }
    return render(request , 'add_manager.html' , context)







@login_required(login_url='login')
def update_manager(request,manager_id):
    manager = Management.objects.get(id=manager_id)
    user = manager.user
    form = UpdateManager(instance=user)

    if request.method == 'POST':
        form = UpdateManager(request.POST,request.FILES,instance=manager)
        print(form.is_valid)
        print(form.error_class)
        if form.is_valid():
            user = CustomUser.objects.update(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                # email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                get_notifications=form.cleaned_data['get_notifications'],
                image=request.FILES.get('image'),
            )
            return redirect('managers')
                
    user_image = request.user.image.url
    manager_image = manager.user.image.url
    username = request.user.username
    
    context = {
        'form': form,
        'user_image': user_image,
        'manager_image': manager_image,
        'username': username
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

    return redirect('task-list')











def guides_list(request):
    guides = Guide.objects.all()
    context = {
        'guides':guides
    }
    return render(request , 'guides_list.html' , context)




def add_guide(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            Guide.objects.create(user=user)
            return redirect('guides_list')
    context = {
        'form' : form
    }
    return render(request , 'add_guide.html' , context)





class UpdateGuideView(TemplateView):
    template_name = 'update_guide.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context
    

def delete_guide(self,request,guide_id):
    Guide.objects.get(id=guide_id).delete()
    return HttpResponse("great")





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




def import_pilgrim(request):
    if request.method == 'POST':
        form = PilgrimForm(request.POST, request.FILES)
        if form.is_valid():
            pilgrim_resource = PilgrimResource()
            dataset = tablib.Dataset().load(request.FILES['file'].read(), format='xlsx')
            result = pilgrim_resource.import_data(dataset, dry_run=True) # Test the data import

            if not result.has_errors():
                pilgrim_resource.import_data(dataset, dry_run=False) # Actually import now
                return HttpResponseRedirect('/success/url/')

    else:
        form = PilgrimForm()
    return render(request, 'import.html', {'form': form})





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

