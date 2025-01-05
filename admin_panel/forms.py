from django.forms import ModelForm , Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from base.models import *
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from base.models import Pilgrim, HajSteps


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
        self.fields['email'] = forms.EmailField(label='الايميل', required=False)
        self.fields['image'] = forms.ImageField(label='الصورة الشخصية', required=False)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)


class NewAdmin(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','image','email','phonenumber','get_notifications']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label=' كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر',required=True,widget=forms.PasswordInput())





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
        self.fields['email'] = forms.EmailField(label='الايميل', required=False)
        self.fields['image'] = forms.ImageField(label='الصورة الشخصية', required=False)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)




class NewGuide(ModelForm):
    class Meta:
        model = Guide
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'] = forms.CharField(label=' كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر',required=True,widget=forms.PasswordInput())
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['email'] = forms.EmailField(label='الايميل', required=False)
        self.fields['image'] = forms.ImageField(label='الصورة الشخصية', required=False)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)




class UpdateManager(forms.ModelForm):
    class Meta:
        model = Management
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['email'] = forms.CharField(label='الايميل', required=False)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)




class UpdateRegisterForm(ModelForm):
    pass




class UpdateEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['email'] = forms.CharField(label='الايميل', required=False)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)



class UpdateUser(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image','username','phonenumber','email','get_notifications']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
    #     self.fields['email'] = forms.CharField(label='الايميل', required=False)
    #     self.fields['username'] = forms.CharField(label='الاسم', required=True)
    #     self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)



class UpdateGuide(forms.ModelForm):
    class Meta:
        model = Guide
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['email'] = forms.CharField(label='الايميل   ', required=False)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)





class CustomUserCreationForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = ['username','get_notifications']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)

    # def clean_password2(self):
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1!= password2:
    #         raise ValidationError(
    #             _("The two password fields didn't match."),
    #             code="password_mismatch",
    #         )
    #     return password2



class UpdatePilgrimForm(forms.ModelForm):
    class Meta:
        model = Pilgrim
        fields = '__all__'
        exclude = ['user','haj_steps','longitude','latitude']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False,initial=self.instance.user.get_notifications)




class TimePickerForm(forms.Form):
    time_field = forms.TimeInput(attrs={'type': 'time'})


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
        self.fields['first_name'] = forms.CharField(label='الاسم', required=False)
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








class NewTask(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'



class NewNote(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class NewRegisterForm(forms.ModelForm):
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data.get('phonenumber')
        if Registration.objects.filter(phonenumber=phonenumber).exists():
            raise forms.ValidationError('رقم الهاتف مسجل مسبقاً')
        return phonenumber

    class Meta:
        model = Registration
        fields = '__all__'
        error_messages = {
            'first_name': {
                'required': 'يرجى إدخال الاسم الأول'
            },
            'father_name': {
                'required': 'يرجى إدخال اسم الأب'
            },
            'grand_father': {
                'required': 'يرجى إدخال اسم الجد'
            },
            'last_name': {
                'required': 'يرجى إدخال اسم العائلة'
            },
            'id_number': {
                'required': 'يرجى إدخال رقم الهوية',
                'invalid': 'رقم الهوية يجب أن يكون أرقاماً فقط'
            },
            'phonenumber': {
                'required': 'يرجى إدخال رقم الهاتف',
                'invalid': 'رقم الهاتف غير صالح'
            },
            'job_position': {
                'required': 'يرجى اختيار المسمى الوظيفي'
            },
            'birthday': {
                'required': 'يرجى إدخال تاريخ الميلاد',
                'invalid': 'صيغة التاريخ غير صحيحة'
            },
            'marital_status': {
                'required': 'يرجى اختيار الحالة الاجتماعية'
            },
            'address': {
                'required': 'يرجى اختيار العنوان'
            },
            'gender': {
                'required': 'يرجى اختيار الجنس'
            },
            'options_trip': {
                'required': 'يرجى اختيار خيارات الرحلة'
            },
            'means_journey': {
                'required': 'يرجى اختيار وسيلة السفر'
            },
            'tawaf': {
                'required': 'يرجى تحديد ما إذا كنت بحاجة لمساعدة في الطواف'
            },
            'sai': {
                'required': 'يرجى تحديد ما إذا كنت بحاجة لمساعدة في السعي'
            },
            'alhajj': {
                'required': 'يرجى اختيار نوع الحج'
            },
            'tradition_reference': {
                'required': 'يرجى اختيار مرجع التقليد'
            },
            'blood_type': {
                'required': 'يرجى اختيار فصيلة الدم'
            },
            'illness': {
                'required': 'يرجى تحديد ما إذا كنت تعاني من أمراض مزمنة'
            },
            'wheelchair': {
                'required': 'يرجى تحديد ما إذا كنت بحاجة لكرسي متحرك'
            },
            'type_help': {
                'required': 'يرجى اختيار نوع المساعدة'
            },
            'tawaf': {
                'required': 'يرجى تحديد ما إذا كنت بحاجة لمساعدة في الطواف'
            },
            'sai': {
                'required': 'يرجى تحديد ما إذا كنت بحاجة لمساعدة في السعي'
            }
        }


class NotificationForm(ModelForm):
    class Meta:
        model = BaseNotification
        fields = '__all__'


class GuidancePostForm(ModelForm):
    class Meta:
        model = GuidancePost
        fields = '__all__'


class GuidanceCategoryForm(ModelForm):
    class Meta:
        model = GuidanceCategory
        fields = '__all__'


class ReligiousPostForm(ModelForm):
    class Meta:
        model = ReligiousPost
        fields = '__all__'


class ReligiousCategoryForm(ModelForm):
    class Meta:
        model = ReligiousCategory
        fields = '__all__'


class StepForm(ModelForm):
    class Meta:
        model = HajSteps
        fields = '__all__'


class SecondaryStepForm(ModelForm):
    class Meta:
        model = SecondarySteps
        fields = '__all__'
