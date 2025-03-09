# healthcare_project/patients/admin.py
from django.contrib import admin
from .models import Patient

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'age', 'blood_group', 'phone_number', 'created_at')
    search_fields = ('user__name', 'blood_group')
    list_filter = ('blood_group',)

admin.site.register(Patient, PatientAdmin)
