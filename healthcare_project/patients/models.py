# healthcare_project/patients/models.py
from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    """
    This is the model for the patient
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patient')
    age = models.IntegerField()
    address = models.CharField(max_length=255)

    blood_group_choices = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=3, choices=blood_group_choices)

    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'patient'
        verbose_name_plural = 'patients'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.name} : {self.age} is a patient with {self.blood_group} blood group"
