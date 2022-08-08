
from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name='home'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('booking/',bookings ,name='booking'),
    path('department/',departments,name='department'),
    path('doctor/',doctors ,name='doctor'),
    path('',login_user ,name='login'),
    path('logout/',logoutUser ,name='logout'),
    path('register/',register ,name='register'),
    ]


