# healthcare_project/doctors/admin.py
from django.contrib import admin
from .models import Doctor

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'specialty', 'experience', 'phone_number', 'created_at')
    search_fields = ('name', 'specialty')
    list_filter = ('specialty',)

admin.site.register(Doctor, DoctorAdmin)
