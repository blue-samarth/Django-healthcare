# healthcare_project/patient_doctor_mapping/models.py
from django.db import models

class PatientDoctorMapping(models.Model):
    patient: models.ForeignKey = models.ForeignKey('patients.Patient', on_delete=models.CASCADE, related_name='patient_doctor_mapping')
    doctor: models.ForeignKey = models.ForeignKey('doctors.Doctor', on_delete=models.CASCADE, related_name='patient_doctor_mapping')
    assigned_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    notes: models.TextField = models.TextField(blank=True, null=True)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('patient', 'doctor')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.patient} - {self.doctor}'