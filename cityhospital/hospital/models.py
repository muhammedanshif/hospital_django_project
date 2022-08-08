from distutils.command.upload import upload
from distutils.text_file import TextFile
from enum import auto
from tkinter import Widget
from django.db import models
from django.forms import CharField

# Create your models here.

class department(models.Model):
    dpt_name =models.CharField(max_length=100)
    dpt_description = models.TextField()

    def __str__(self):
        return self.dpt_name

class doctor(models.Model):
    doc_name = models.CharField(max_length=30)
    doc_spec = models.CharField(max_length=100)
    dpt_name = models.ForeignKey("department",  on_delete=models.CASCADE)
    doc_image = models.ImageField(upload_to = 'doctors')

    def __str__(self):
        return 'dr ' + self.doc_name +'-('+ self.doc_spec + ')'

class booking(models.Model):
    p_name = models.CharField(max_length=30)
    p_phone = models.IntegerField()
    p_email = models.EmailField()
    doc_name = models.ForeignKey("doctor",on_delete=models.CASCADE)
    booking_date = models.DateField()
    booked_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.p_name

class login_admin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=30)
    def __str__(self):
        return self.username
class register(models.Model):
    f_name = models.CharField(max_length=25)
    l_name = models.CharField(max_length=25)
    password = models.CharField(max_length=30) 
    def __str__(self):
        return self.f_name + self.l_name
   
