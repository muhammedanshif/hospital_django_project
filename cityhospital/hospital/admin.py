from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(department)
admin.site.register(doctor)
admin.site.register(login_admin)
admin.site.register(register)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id','p_name','p_phone','p_email','doc_name','booking_date','booked_on')
admin.site.register(booking,BookingAdmin)