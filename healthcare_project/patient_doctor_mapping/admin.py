# healthcare_project/patient_doctor_mapping/admin.py
from django.contrib import admin
from .models import PatientDoctorMapping

class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'assigned_at', 'created_at')
    search_fields = ('patient__user__name', 'doctor__name')
    list_filter = ('assigned_at',)

admin.site.register(PatientDoctorMapping, PatientDoctorMappingAdmin)
