from typing import Any
from django.shortcuts import render , HttpResponse , redirect , HttpResponseRedirect
from django.views.generic import TemplateView
from base.models import *
from base.resources import PilgrimResource , RegistrationResource , UserPasswordResource
from .forms import *
from .forms import PilgrimForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
import pandas as pd
from django.core.files.storage import default_storage
from django.db import transaction
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from base.utils.notifications import send_event_notification
from phonenumber_field.phonenumber import PhoneNumber
from django.core.validators import MinValueValidator, MaxValueValidator , RegexValidator




def login_user(request):
    if request.method == 'POST':
        phonenumber = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=phonenumber, password=password)
        if user is not None:
            login(request,user)
            return redirect('main_dashboard')

    return render(request , 'login.html')




@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')




def change_password(request,user_id):
    if request.method == 'POST':
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 and password2:
                user = CustomUser.objects.get(id=user_id)
                user.set_password(password1)
                user.save()
                return redirect('main_dashboard') 
        
    return render(request, 'change_password.html')



@login_required(login_url='login')
def main_dashboard(request):
    total_pilgrims = Pilgrim.objects.count()
    total_employees = Employee.objects.count()
    total_managers = Management.objects.count()
    total_guides = Guide.objects.count()
    total_forms = Registration.objects.count()

    context = {
    'total_pilgrims' : total_pilgrims,
    'total_employees' : total_employees,
    'total_managers' : total_managers,
    'total_guides' : total_guides,
    'total_forms' : total_forms,
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
    forms = Registration.objects.filter(first_name__startswith = q).order_by('-id')

    context = {
        'forms':forms,
 }
    return render(request , 'registration_forms.html' , context)





@login_required(login_url='login')
def add_register_form(request):
    form = NewRegisterForm()


    if request.method == 'POST':
        form = NewRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_forms')

    context = {
        'form': form,
    }
    return render(request, 'add_form.html', context)





@login_required(login_url='login')
def update_register_form(request,form_id):
    register_form = Registration.objects.get(id=form_id)
    form = NewRegisterForm(instance=register_form)

    if request.method == 'POST':
        form = NewRegisterForm(request.POST,instance=register_form)
        if form.is_valid():
            form.save()
            return redirect('registration_forms')

    context = {
        'form': form,
    }
    return render(request, 'add_form.html', context)






def delete_register_form(request,form_id):
    Registration.objects.get(id=form_id).delete()

    return redirect('registration_forms')








@login_required(login_url='login')
def pilgrims_list(request):
    q = request.GET.get('q') or ''
    pilgrims = Pilgrim.objects.filter(first_name__startswith = q).order_by('-id')

    context = {
        'pilgrims':pilgrims,
    }
    return render(request , 'pilgrims_list.html' , context)





def update_pilgrim(request,pilgrim_id):
        pilgrim = Pilgrim.objects.get(id=pilgrim_id)
        user = CustomUser.objects.get(id=pilgrim.user.id)
        form = PilgrimForm(instance=pilgrim)

        if request.method == 'POST':
            
            pilgrim_form = PilgrimForm(request.POST,request.FILES,instance=pilgrim)

            if pilgrim_form.is_valid():
                pilgrim = pilgrim_form.save(commit=False)
                user.get_notifications = pilgrim_form.cleaned_data['get_notifications']
                user.phonenumber = pilgrim_form.cleaned_data['phonenumber']
                user.username = request.POST['first_name'] + ' ' + request.POST['father_name'] + ' ' + request.POST['grand_father'] + ' ' + request.POST['last_name']
                user.save()
                pilgrim.haj_steps.set(request.POST.getlist('haj_steps'))
                pilgrim.save()

            return redirect('pilgrims')

        try:
            pilgrim_image = pilgrim.user.image.url
        except:
            pilgrim_image = ' '

        context = { 'form': form,
                    'pilgrim_image':pilgrim_image,
                    'user_id': user.id, 
                    'company_logo':pilgrim.company_logo.url
                    }

        return render(request, 'update_pilgrim.html', context=context)






@login_required(login_url='login')
def add_pilgrim(request):
    form = NewPilgrim()

    if request.method == 'POST':
        form = NewPilgrim(request.POST, request.FILES)
        if form.is_valid():
            print(form.error_class)
            user = CustomUser.objects.create(
                username=form.cleaned_data['first_name'],
                phonenumber=form.cleaned_data['phonenumber'],
                # email=form.cleaned_data['email'],
                get_notifications=form.cleaned_data['get_notifications'],
                user_type = 'حاج'
            )
            user.set_password(form.cleaned_data['password'])
            if request.POST['image']:
                user.image = request.POST['image']
                user.save()

            Chat.objects.create(user=user , chat_type='guide')
            Chat.objects.create(user=user , chat_type='manager')

            pilgrim = Pilgrim.objects.create(
                user=user,
                first_name=form.cleaned_data['first_name'],
                father_name=form.cleaned_data['father_name'],
                last_name=form.cleaned_data['last_name'],
                grand_father=form.cleaned_data['grand_father'],
                registeration_id=form.cleaned_data['registeration_id'],
                phonenumber=form.cleaned_data['phonenumber'],
                hotel=form.cleaned_data['hotel'],
                hotel_address=form.cleaned_data['hotel_address'],
                room_num=form.cleaned_data['room_num'],
                gate_num=form.cleaned_data['gate_num'],
                flight_num=form.cleaned_data['flight_num'],
                flight_date=request.POST['flight_date'],
                flight_company = form.cleaned_data['flight_company'],
                from_city=form.cleaned_data['from_city'],
                to_city=form.cleaned_data['to_city'],
                birthday=request.POST['birthday'],
                duration=form.cleaned_data['duration'],
                boarding_time=request.POST['boarding_time'],
                arrival=request.POST['arrival'],
                departure=request.POST['departure'],
            )
            if request.POST['guide']:
                guide = Guide.objects.get(id=request.POST['guide'])
                pilgrim.guide = guide
                pilgrim.save()

            return redirect('pilgrims')
        
        else:
            return redirect('add_pilgrim')
    

    context = {
        'form': form,
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
def delete_pilgrim(request,pilgrim_id):
    pilgrim = Pilgrim.objects.get(id=pilgrim_id)
    user = CustomUser.objects.get(id=pilgrim.user.id)
    user.delete()
    
    return redirect('pilgrims')






@login_required(login_url='login')
def managers_list(request):
    q = request.GET.get('q') or ''
    managers = Management.objects.filter(user__first_name__startswith = q).order_by('-id')
    context = {
        'managers':managers,
    }
    return render(request , 'managers_list.html' , context)








@login_required(login_url='login')
def add_manager(request):
    form = NewManager()

    if request.method == 'POST':
        form = NewManager(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['password1'])
            user = CustomUser.objects.create(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                email=form.cleaned_data['email'],
                get_notifications=form.cleaned_data['get_notifications'],
                user_type = 'اداري'
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            if form.cleaned_data['image']:
                user.image = form.cleaned_data['image']
            
            Management.objects.create(user=user)
            return redirect('managers')
    context = {
        'form' : form,
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
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('managers')

    user_image = request.user.image.url
    manager_image = manager.user.image.url
    username = request.user.username
    
    context = {
        'form': form,
        'manager_image': manager_image,
        'user_id': user.id,
    }
    return render(request, 'update_manager.html', context)




@login_required(login_url='login')
def delete_manager(request,manager_id):
    manager = Management.objects.get(id=manager_id)
    user = CustomUser.objects.get(id=manager.user.id)
    user.delete()
    return redirect("managers")










@login_required(login_url='login')
def task_list(request):
    q = request.GET.get('q') or ''
    tasks = Task.objects.filter(title__startswith = q).order_by('-id')

    context = {
        'tasks':tasks,
 }
    return render(request , 'tasks.html' , context)








@login_required(login_url='login')
def add_task(request):
    form = NewTask()

    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form,
    }
    return render(request, 'add_task.html', context)







@login_required(login_url='login')
def update_task(request,task_id):
    task = Task.objects.get(id=task_id)
    form = NewTask(instance=task)

    if request.method == 'POST':
        form = NewTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('tasks')

    context = {
        'form': form,
    }
    return render(request, 'add_task.html', context)







@login_required(login_url='login')
def delete_task(request,task_id):
    Task.objects.get(id=task_id).delete()

    return redirect('tasks')







@login_required(login_url='login')
def notes_list(request):
    q = request.GET.get('q') or ''
    notes = Note.objects.filter(pilgrim__user__username__startswith = q).order_by('-id')

    context = {
        'notes':notes,
 }
    return render(request , 'notes.html' , context)





@login_required(login_url='login')
def add_note(request):
    form = NewNote()

    if request.method == 'POST':
        form = NewNote(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')

    context = {
        'form': form,
    }
    return render(request, 'add_note.html', context)







@login_required(login_url='login')
def update_note(request,note_id):
    note = Note.objects.get(id=note_id)
    form = NewNote(instance=note)

    if request.method == 'POST':
        form = NewNote(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes')

    context = {
        'form': form,
    }
    return render(request, 'add_note.html', context)







@login_required(login_url='login')
def delete_note(request,note_id):
    Note.objects.get(id=note_id).delete()

    return redirect('notes')















@login_required(login_url='login')
def employees_list(request):
    q = request.GET.get('q') or ''

    employees = Employee.objects.filter(user__username__startswith=q).order_by('-id')
    context = {
        'employees':employees,
    }
    return render(request , 'employees_list.html' , context)



@login_required(login_url='login')
def add_employee(request):
    form = NewEmployee()

    if request.method == 'POST':
        form = NewEmployee(request.POST, request.FILES)
        if form.is_valid():
            user = CustomUser.objects.create(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                email=form.cleaned_data['email'],
                get_notifications=form.cleaned_data['get_notifications'],
                user_type = 'موظف'
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            if form.cleaned_data['image']:
                user.image = form.cleaned_data['image']

            Employee.objects.create(user=user)
            return redirect('employees')
    context = {
        'form' : form,
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
            image=request.FILES.get('image')
            print(image)
            if image:
                user.image = request.FILES.get('image')
            else:
                user.image = employee.user.image


            user.get_notifications = form.cleaned_data['get_notifications']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('employees')

    employee_image = employee.user.image.url
    
    context = {
        'form': form,
        'user_id': user.id,
        'employee_image': employee_image,
    }
    return render(request, 'update_employee.html', context)








@login_required(login_url='login')
def delete_employee(request,employee_id):
    employee = Employee.objects.get(id=employee_id)
    user = CustomUser.objects.get(id=employee.user.id)
    user.delete()
    return redirect('employees')






@login_required(login_url='login')
def guides_list(request):
    q = request.GET.get('q') or ''

    guides = Guide.objects.filter(user__username__startswith=q).order_by('-id')
    context = {
        'guides':guides,
    }
    return render(request , 'guides_list.html' , context)



@login_required(login_url='login')
def add_guide(request):
    form = NewGuide()

    if request.method == 'POST':
        form = NewGuide(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['image'])
            user = CustomUser.objects.create(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                email=form.cleaned_data['email'],
                get_notifications=form.cleaned_data['get_notifications'],
                user_type = 'مرشد'
            )
            user.set_password(form.cleaned_data['password1'])
            user.save()
            if form.cleaned_data['image']:
                user.image = form.cleaned_data['image'] 

            Guide.objects.create(user=user)
            return redirect('guides')
    context = {
        'form' : form,

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
            image=request.FILES.get('image')
            if image:
                user.image = request.FILES.get('image')
            else:
                user.image = guide.user.image


            user.get_notifications = form.cleaned_data['get_notifications']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('guides')

    guide_image = guide.user.image.url
    
    context = {
        'form': form,
        'guide_image': guide_image,
        'user_id': user.id,
    }
    return render(request, 'update_guide.html', context)


    

def delete_guide(request,guide_id):
    guide = Guide.objects.get(id=guide_id)
    user = CustomUser.objects.get(id=guide.user.id)
    user.delete()
    return redirect('guides')








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
            df = pd.read_excel(excel_file)
            for index, row in df.iterrows():

                arrival_datetime = datetime.strptime(str(row['موعد الوصول']), '%H:%M:%S')
                departure_datetime = datetime.strptime(str(row['موعد الرحيل']), '%H:%M:%S')

                diff = departure_datetime - arrival_datetime

                formatted_diff = str(timedelta(hours=diff.seconds//3600, minutes=diff.seconds//60%60))
                pilgrim_phonenumber = PhoneNumber.from_string(str(row['رقم الجوال']) , region='SA')
                pilgrim_username = str(row['الاسم الأول']) + ' ' + str(row['اسم الأب']) + ' ' + str(row['اسم الجد']) + ' ' + str(row['العائلة'])
                user , created =CustomUser.objects.update_or_create(phonenumber=pilgrim_phonenumber ,
                                                                    defaults={
                                                                    'username':pilgrim_username,
                                                                    'user_type':'حاج',
                                                                    'first_name':str(row['الاسم الأول']) , 
                                                                    'last_name':str(row['العائلة'])   
                                                                    })
                if created:                
                    my_password = generate_password()
                    user.set_password(my_password)
                    user.save()
                    chat1 = Chat.objects.create(user=user , chat_type='guide')
                    chat2 = Chat.objects.create(user=user , chat_type='manager')
                    UserPassword.objects.create(password=my_password , username=user.username , phonenumber=str(user.phonenumber))
                else:
                    user.first_name = row['الاسم الأول']
                    user.last_name = row['العائلة']

                pilgrim , created = Pilgrim.objects.update_or_create(
                    user=user,
                    phonenumber=pilgrim_phonenumber,
                    defaults={
                    'registeration_id':row['رقم الهوية'],
                    'first_name':row['الاسم الأول'],
                    'father_name':row['اسم الأب'],
                    'grand_father':row['اسم الجد'],
                    'last_name':row['العائلة'],
                    'birthday':row['تاريخ الميلاد - الميلادي فقط'],
                    'flight_num':row['رقم الرحلة'],
                    'flight_date':row['تاريخ الرحلة'],
                    'arrival':row['موعد الوصول'],
                    'departure':row['موعد الرحيل'],
                    'from_city':row['من المدينة'],
                    'to_city':row['إلى المدينة'],
                    'duration':str(formatted_diff),
                    'boarding_time':row['وقت الصعود'],
                    'gate_num':row['رقم البوابة'],
                    'flight_company':row['شركة الطيران'],
                    'status':True,
                    'hotel':row['الفندق'],
                    'hotel_address':row['عنوان الفندق'],
                    'room_num':33
                    }
                )
                pilgrim.save()

            passwords = UserPasswordResource()
            dataset = passwords.export()
            response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="passwords.xlsx"'
            return response

            # return redirect('pilgrims')
        return render(request, 'import_pilgrims.html')






def notifications_list(request):
    q = request.GET.get('q') or ''
    notifications = BaseNotification.objects.filter(title__startswith=q).order_by('-id')
    context = {
        'notifications':notifications,
    }
    return render(request , 'notifications_list.html' , context)







@login_required(login_url='login')
def add_notification(request):
    form = NotificationForm()
    if request.method == 'POST':
        form = NotificationForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            send_event_notification(title=title,content=content)
            form.save()
            return redirect('notifications')
    context = {
        'form' : form,
    }
    return render(request , 'add_notification.html' , context)

    


def delete_notifications(request,notification_id):
    BaseNotification.objects.get(id=notification_id).delete()
    return redirect('notifications')







def guidance_posts(request):
    q = request.GET.get('q') or ''
    posts = GuidancePost.objects.filter(title__startswith=q).order_by('-id')
    context = {
        'posts':posts,
    }
    return render(request , 'guidance_posts.html' , context)






@login_required(login_url='login')
def add_guidance_post(request):
    form = GuidancePostForm()
    if request.method == 'POST':
        form = GuidancePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('guidance_posts')
    context = {
        'form' : form,
    }
    return render(request , 'add_guidance_post.html' , context)





@login_required(login_url='login')
def update_guidance_post(request,post_id):
    post = GuidancePost.objects.get(id=post_id)
    form = GuidancePostForm(instance=post)

    if request.method == 'POST':
        form = GuidancePostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('guidance_posts')

    context = {
        'form': form,
        'post_image':post.cover.url
    }
    return render(request, 'update_guidance_post.html', context)





@login_required(login_url='login')
def delete_guidance_post(request,post_id):
    GuidancePost.objects.get(id=post_id).delete()
    return redirect('guidance_posts')






def guidance_categories(request): 
    q = request.GET.get('q') or ''
    categories = GuidanceCategory.objects.filter(name__startswith=q).order_by('-id')
    context = {
        'categories':categories,
    }
    return render(request , 'guidance_categories.html' , context)




@login_required(login_url='login')
def add_guidance_category(request):
    form = GuidanceCategoryForm()
    if request.method == 'POST':
        form = GuidanceCategoryForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('guidance_categories')
    context = {
        'form' : form,
    }
    return render(request , 'add_guidance_category.html' , context)








@login_required(login_url='login')
def update_guidance_category(request,category_id):
    category = GuidanceCategory.objects.get(id=category_id)
    form = GuidanceCategoryForm(instance=category)

    if request.method == 'POST':
        form = GuidanceCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('guidance_categories')

    context = {
        'form': form,
    }
    return render(request, 'add_guidance_category.html', context)





@login_required(login_url='login')
def delete_guidance_category(request,category_id):
    GuidanceCategory.objects.get(id=category_id).delete()
    return redirect('guidance_categories')








def religious_posts(request):
    q = request.GET.get('q') or ''
    posts = ReligiousPost.objects.filter(title__startswith=q).order_by('-id')
    context = {
        'posts':posts,
    }
    return render(request , 'religious_posts.html' , context)






@login_required(login_url='login')
def add_religious_post(request):
    form = ReligiousPostForm()
    if request.method == 'POST':
        form = ReligiousPostForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('religious_posts')
    context = {
        'form' : form,
    }
    return render(request , 'add_religious_post.html' , context)









@login_required(login_url='login')
def update_religious_post(request,post_id):
    post = ReligiousPost.objects.get(id=post_id)
    form = ReligiousPostForm(instance=post)

    if request.method == 'POST':
        form = ReligiousPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('religious_posts')

    context = {
        'form': form,
        'post_image':post.cover.url
    }
    return render(request, 'update_religious_post.html', context)





@login_required(login_url='login')
def delete_religious_post(request,post_id):
    ReligiousPost.objects.get(id=post_id).delete()
    return redirect('religious_posts')







def religious_categories(request): 
    q = request.GET.get('q') or ''
    categories = ReligiousCategory.objects.filter(name__startswith=q).order_by('-id')
    context = {
        'categories':categories,
    }
    return render(request , 'religious_categories.html' , context)






@login_required(login_url='login')
def add_religious_category(request):
    form = ReligiousCategoryForm()

    if request.method == 'POST':
        form = ReligiousCategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('religious_categories')
    context = {
        'form' : form,
    }
    return render(request , 'add_religious_category.html' , context)





@login_required(login_url='login')
def update_religious_category(request,category_id):
    category = ReligiousCategory.objects.get(id=category_id)
    form = ReligiousCategoryForm(instance=category)

    if request.method == 'POST':
        form = ReligiousCategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('religious_categories')

    context = {
        'form': form,
    }
    return render(request, 'add_religious_category.html', context)





@login_required(login_url='login')
def delete_religious_category(request,category_id):
    ReligiousCategory.objects.get(id=category_id).delete()
    return redirect('religious_categories')





@login_required(login_url='login')
def update_religious_post(request,post_id):
    post = ReligiousPost.objects.get(id=post_id)
    form = ReligiousPostForm(instance=post)

    if request.method == 'POST':
        form = ReligiousPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('religious_posts')

    context = {
        'form': form,
        'post_image':post.cover.url
    }
    return render(request, 'update_religious_post.html', context)





@login_required(login_url='login')
def delete_religious_post(request,post_id):
    ReligiousPost.objects.get(id=post_id).delete()
    return redirect('religious_posts')





@login_required(login_url='login')
def steps_list(request):
    q = request.GET.get('q') or ''
    steps = HajSteps.objects.filter(name__startswith=q).order_by('-id')
    context = {
        'steps':steps,
    }
    return render(request , 'steps.html' , context)






@login_required(login_url='login')
def add_step(request):
    form = StepForm()

    if request.method == 'POST':
        form = StepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('steps')
    context = {
        'form' : form,
    }
    return render(request , 'add_step.html' , context)





@login_required(login_url='login')
def update_step(request,step_id):
    step = HajSteps.objects.get(id=step_id)
    form = StepForm(instance=step)

    if request.method == 'POST':
        form = StepForm(request.POST, instance=step)
        if form.is_valid():
            form.save()
            return redirect('steps')

    context = {
        'form': form,
    }
    return render(request, 'add_step.html', context)





@login_required(login_url='login')
def delete_step(request,step_id):
    HajSteps.objects.get(id=step_id).delete()
    return redirect('steps')









@login_required(login_url='login')
def secondary_steps_list(request):
    q = request.GET.get('q') or ''
    steps = SecondarySteps.objects.filter(name__startswith=q).order_by('-id')
    context = {
        'steps':steps,
    }
    return render(request , 'secondary_steps.html' , context)











@login_required(login_url='login')
def add_secondary_step(request):
    form = SecondaryStepForm()

    if request.method == 'POST':
        form = SecondaryStepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('secondary_steps')
    context = {
        'form' : form,
    }
    return render(request , 'add_secondary_step.html' , context)







@login_required(login_url='login')
def update_secondary_step(request,step_id):
    step = SecondarySteps.objects.get(id=step_id)
    form = SecondaryStepForm(instance=step)

    if request.method == 'POST':
        form = StepForm(request.POST, instance=step)
        if form.is_valid():
            form.save()
            return redirect('secondary_steps')

    context = {
        'form': form,
    }
    return render(request, 'add_secondary_step.html', context)








@login_required(login_url='login')
def delete_secondary_step(request,step_id):
    SecondarySteps.objects.get(id=step_id).delete()
    return redirect('secondary_steps')





def my_account(request):
    user = request.user
    form = UpdateUser(instance=user)

    if request.method == 'POST':
        form = UpdateUser(request.POST,request.FILES,instance=user)
        if form.is_valid():
            user = CustomUser.objects.get(
                phonenumber=form.cleaned_data['phonenumber'],
            )
            image=request.FILES.get('image')
            if image:
                user.image = request.FILES.get('image')
            else:
                user.image = user.image


            user.get_notifications = form.cleaned_data['get_notifications']
            user.username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.save()
            return redirect('employees')

    
    context = {
        'form': form,
        'user_id': user.id,
    }
    
    return render(request , 'my_account.html' , context=context)







@login_required(login_url='login')
def add_admin(request):
    form = NewAdmin()

    if request.method == 'POST':
        form = NewAdmin(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            user = CustomUser.objects.create(
                username=form.cleaned_data['username'],
                phonenumber=form.cleaned_data['phonenumber'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1'],
                get_notifications=form.cleaned_data['get_notifications'],
                user_type = 'اداري',
                is_superuser = True,
                is_staff = True
            )
            if form.cleaned_data['image']:
                user.image = form.cleaned_data['image']
            
            return redirect('main_dashboard')
    context = {
        'form' : form,
    }
    return render(request , 'add_admin.html' , context)


