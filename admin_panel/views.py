from typing import Any
from django.shortcuts import render , HttpResponse , redirect
from django.views.generic import TemplateView
from base.models import *
from base.resources import PilgrimResource
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
def notifications(request):
    context ={
        
    }
    return render(request , 'notifications.html' , context=context)


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
def tasks(request):
    tasks = Task.objects.all()
    context ={
        'tasks':tasks
    }
    return render(request , 'tasks.html' , context=context)



class AdminListView(TemplateView):
    template_name = 'admin_list.html'


class UpdateAdminView(TemplateView):
    template_name = 'update_admin.html'




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
        if form.is_valid():
            user = CustomUser.objects.create_user(
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
                departure=form.cleaned_data['departure'],
                arrival=form.cleaned_data['arrival'],
            )

            pilgrim.save()
            return redirect('pilgrims_list')
    

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


class UpdatePilgrimView(TemplateView):
    template_name = 'users/customer/update_pilgrim.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context

@login_required(login_url='login')
def delete_pilgrim(request,pilgrim_id):
    Pilgrim.objects.get(id=pilgrim_id).delete()
    return HttpResponse("greate")





def managers_list(request):
    managers = Management.objects.filter().order_by('-id')
    context = {
        'managers':managers
    }
    return render(request , 'managers_list.html' , context)




def add_manager(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            Management.objects.create(user=user)
            return redirect('managers_list')
    context = {
        'form' : form
    }
    return render(request , 'add_manager.html' , context)




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
def delete_task(request,task_id):
    Task.objects.get(id=task_id).delete()

    return redirect('task-list')





class AddPilgrimView(TemplateView):
    template_name = 'users/customer/add_pilgrim.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


class UpdatePilgrimView(TemplateView):
    template_name = 'users/customer/update_pilgrim.html'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        return context


def delete_manager(request,manager_id):
    Management.objects.get(id=manager_id).delete()
    return HttpResponse("greate")






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






def employees_list(request):
    employees = Employee.objects.all()
    context = {
        'employees':employees
    }
    return render(request , 'employees_list.html' , context)




def add_employee(request):
    form = NewUser()
    if request.method == 'POST':
        form = NewUser(request.POST)
        if form.is_valid():
            user = form.save()
            Employee.objects.create(user=user)
            return redirect('employees_list')
    context = {
        'form' : form
    }
    return render(request , 'users/employee/add_employee.html' , context)


    

def delete_employee(self,request,employee_id):
    Employee.objects.get(id=employee_id).delete()
    return HttpResponse("great")





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