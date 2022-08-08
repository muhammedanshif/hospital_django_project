from dataclasses import field
import django




from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class DateInput(forms.DateInput):
    input_type ='date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__' 

        widgets = {
            'booking_date' : DateInput,
        }

        labels = {
            'p_name' : "Patient Name",
            'p_phone': "Phone number",
            'p_email' :"Email",
            'doc_name' :"Doctor name",
            'booking_date' :"Booking date",

        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = login_admin;
        fields = '__all__'

        widgets = {
            'username' : forms.TextInput(attrs={'class':'form-control'}),
            'password' : forms.PasswordInput(attrs={'class':'form-control'})
            }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']