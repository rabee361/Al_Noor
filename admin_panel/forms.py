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
    class Meta:
        model = CustomUser
        fields = ["username","phonenumber","password1","password2","email","get_notifications","image"]
       




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



class UpdateAdmin(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','phonenumber','email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['phonenumber'] = forms.CharField(label='رقم الهاتف', required=True)
        self.fields['email'] = forms.CharField(label='الايميل   ', required=False)
        self.fields['username'] = forms.CharField(label='الاسم', required=True)



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
        self.fields['first_name'] = forms.CharField(label='الاسم', required=False)
        self.fields['image'] = forms.ImageField(label='الصورة الشخصية', required=False)
        self.fields['get_notifications'] = forms.BooleanField(label='تلقي اشعارات', required=False)





class NewTask(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'


class NewNote(ModelForm):
    pilgrim = forms.ModelChoiceField(queryset=Pilgrim.objects.filter(user__is_deleted=False), required=True, label="الحاج" , widget=forms.Select(attrs={'class': 'form-control' , 'id': 'pilgrim-select'}))
    guide = forms.ModelChoiceField(queryset=Guide.objects.filter(user__is_deleted=False), required=True, label="المرشد" , widget=forms.Select(attrs={'class': 'form-control' , 'id': 'guide-select'}))
    
    class Meta:
        model = Note
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        pilgrim = cleaned_data.get('pilgrim')
        guide = cleaned_data.get('guide')

        if pilgrim and not Pilgrim.objects.filter(id=pilgrim.id).exists():
            raise forms.ValidationError('الحاج غير موجود')
        if guide and not Guide.objects.filter(id=guide.id).exists():
            raise forms.ValidationError('المرشد غير موجود')

        return cleaned_data



class NewRegisterForm(forms.ModelForm):
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data.get('phonenumber')
        if Registration.objects.filter(phonenumber=phonenumber, is_deleted=False).exists():
            raise forms.ValidationError('رقم الهاتف مسجل مسبقاً')
        elif Registration.objects.filter(phonenumber=phonenumber, is_deleted=True).exists():
            form = Registration.objects.get(phonenumber=phonenumber, is_deleted=True)
            form.delete()
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
            'additional': {
                'required': 'يرجى كتابة المرافق معاك'
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
        }







class UpdateRegisterForm(forms.ModelForm):

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
            'additional': {
                'required': 'يرجى كتابة المرافق معاك'
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
        }







class NotificationForm(ModelForm):
    class Meta:
        model = BaseNotification
        fields = ['title','content']


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

 
class PilgrimCreationForm(forms.ModelForm):
    password = forms.CharField(
        label='كلمة السر',
        widget=forms.PasswordInput(),
        error_messages={'required': 'يرجى إدخال كلمة السر'}
    )
    password2 = forms.CharField(
        label='تأكيد كلمة السر',
        widget=forms.PasswordInput(),
        error_messages={'required': 'يرجى تأكيد كلمة السر'}
    )
    get_notifications = forms.BooleanField(
        label='تلقي اشعارات',
        required=False
    )
    image = forms.ImageField(
        label='الصورة الشخصية',
        required=False
    )

    class Meta:
        model = Pilgrim
        fields = [
            'first_name', 'father_name', 'last_name', 'grand_father',
            'registeration_id', 'phonenumber', 'hotel', 'hotel_address',
            'room_num', 'gate_num', 'flight_num', 'flight_date',
            'flight_company', 'company_logo', 'from_city', 'to_city',
            'birthday', 'duration', 'boarding_time', 'arrival', 'departure',
            'guide'
        ]
        error_messages = {
            'first_name': {'required': 'يرجى إدخال الاسم الأول'},
            'father_name': {'required': 'يرجى إدخال اسم الأب'},
            'last_name': {'required': 'يرجى إدخال اسم العائلة'},
            'grand_father': {'required': 'يرجى إدخال اسم الجد'},
            'registeration_id': {'required': 'يرجى إدخال رقم التسجيل'},
            'phonenumber': {'required': 'يرجى إدخال رقم الهاتف'},
            'hotel': {'required': 'يرجى إدخال اسم الفندق'},
            'hotel_address': {'required': 'يرجى إدخال عنوان الفندق'},
            'room_num': {'required': 'يرجى إدخال رقم الغرفة'},
            'flight_num': {'required': 'يرجى إدخال رقم الرحلة'},
            'flight_date': {'required': 'يرجى إدخال تاريخ الرحلة'},
            'flight_company': {'required': 'يرجى إدخال شركة الطيران'},
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('كلمات المرور غير متطابقة')
        return password2

    def clean_phonenumber(self):
        phonenumber = self.cleaned_data.get('phonenumber')
        if CustomUser.objects.filter(phonenumber=phonenumber).exists():
            raise forms.ValidationError('رقم الهاتف مسجل مسبقاً')
        return phonenumber


class LiveStreamForm(ModelForm):
    class Meta:
        model = LiveStream
        fields = '__all__'


class LiveStreamTypeForm(ModelForm):
    class Meta:
        model = LiveStreamCategory
        fields = '__all__'


class TermsForm(ModelForm):
    class Meta:
        model = TermsAndConditions
        fields = '__all__'
