

import imp
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')
@login_required(login_url='login')
def about(request):
    return render(request,'about.html')
@login_required(login_url='login')
def bookings(request):
    if request.method =="POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    form = BookingForm()
    dict_form = {
        'form' : form
    }
    return render(request,'booking.html',dict_form)

def contact(request):
    dict_docs = {
        'booking' : booking.objects.all(),
        'doctors'  : doctor.objects.all()
    }
    return render(request,'contact.html',dict_docs)

   

def departments(request):

    dict_dpt = {
        'dept' : department.objects.all()
    }
    return render(request,'departments.html',dict_dpt)

def doctors(request):
    dict_docs = {
        'doctors' : doctor.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def login_user(request):
    if request.method =="POST":
       username= request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request,username=username , password=password)
       if user is not None:
             login(request,user)
             return redirect('home')
       else:
         messages.info(request,'Username OR password is incorrect')
         
    context ={}
    return render(request,'login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
         form.save()
         user = form.cleaned_data.get('username')
         messages.success(request,'Account was created for ' + user)

         return redirect('login')
    
    context ={'form':form}
    return render(request,'register.html',context)