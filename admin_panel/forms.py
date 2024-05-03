from django.forms import ModelForm , Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from base.models import *


class NewUser(UserCreationForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="الاسم")
    # phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="رقم الهاتف")
    # email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="الايميل")
    # image = forms.ImageField()
    # get_notifications = forms.BooleanField()
        
    class Meta:
        model = CustomUser
        fields = ["username","phonenumber","password1","password2","email","get_notifications","image"]
        
    # def clean(self):
    #     cleaned_data = super().clean()
        # phonenumber = cleaned_data.get('phonenumber')
        # if phonenumber and not phonenumber.isdigit():
        #     self.add_error('phonenumber', 'رقم الهاتف يجب أن يكون أرقام فقط.')

        # password1 = cleaned_data.get('password1')
        # password2 = cleaned_data.get('password2')
        # if password1 != password2:
        #     self.add_error('password2', 'كلمات المرور المرور غير متطابقة.')






class NewManager(forms.ModelForm):
    class Meta:
        model = Management
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label=' كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['image'] = forms.ImageField(label='الصورة الشخصية', required=True)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)





class NewEmployee(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label=' كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['image'] = forms.ImageField(label='الصورة الشخصية', required=True)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)




class UpdateManager(forms.ModelForm):
    class Meta:
        model = Management
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label=' كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)



class UpdateEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label=' كلمة السر',widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر',widget=forms.PasswordInput())
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)






class NewPilgrim(forms.ModelForm):
    class Meta:
        model = Pilgrim
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'] = forms.CharField(label=' كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر',required=True,widget=forms.PasswordInput())
        # self.fields['email'] = forms.EmailField(label='تأكيد كلمة السر', required=False)
        # self.fields['first_name'] = forms.CharField(label='الاسم', required=False)
        self.fields['image'] = forms.ImageField(label='الصورة الشخصية', required=False)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)


    # def clean(self):
    #     cleaned_data = super().clean()
    #     phonenumber = cleaned_data.get('phonenumber')
    #     if phonenumber and not phonenumber.isdigit():
    #         self.add_error('phonenumber', 'رقم الهاتف يجب أن يكون أرقام فقط.')

    #     password1 = cleaned_data.get('password1')
    #     password2 = cleaned_data.get('password2')
    #     if password1 and password2 and password1 != password2:
    #         self.add_error('password2', 'كلمات المرور المرور غير متطابقة.')



class PilgrimForm(forms.Form):
    file = forms.FileField()







class NewTask(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'



class NewRegisterForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'



class NotificationForm(ModelForm):
    class Meta:
        model = BaseNotification
        fields = '__all__'


class GuidancePostForm(ModelForm):
    class Meta:
        model = GuidancePost
        fields = '__all__'
