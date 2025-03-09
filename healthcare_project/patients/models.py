# healthcare_project/patients/models.py
from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    """
    This is the model for the patient
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    age = models
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'patients'

    def __str__(self):
        return f"{self.user.name} - {self.user.email} is a patient"
