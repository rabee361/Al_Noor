from django.forms import ModelForm , Form
from django import forms
from django.contrib.auth.forms import UserCreationForm
from base.models import *


class NewUser(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),label="الاسم")
    phonenumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="رقم الهاتف")
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), label="الايميل")
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'type' : 'password'}), label="كلمة المرور")
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control' , 'type' : 'password'}) , label="تأكيد كملة المرور")

        
    class Meta:
        model = CustomUser
        fields = ("username","phonenumber","email","password1","password2")
        
    def clean(self):
        cleaned_data = super().clean()
        phonenumber = cleaned_data.get('phonenumber')
        if phonenumber and not phonenumber.isdigit():
            self.add_error('phonenumber', 'رقم الهاتف يجب أن يكون أرقام فقط.')

        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            self.add_error('password2', 'كلمات المرور المرور غير متطابقة.')




class NewPilgrim(forms.ModelForm):
    class Meta:
        model = Pilgrim
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'] = forms.CharField(label='كلمة السر', required=False)
        self.fields['password2'] = forms.CharField(label='تأكيد كلمة السر', required=False)
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
