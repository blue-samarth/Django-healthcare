# healthcare_project/doctors/models.py
from django.db import models
from django.conf import settings

class Doctor(models.Model):
    """
    This class represents a Doctor model. 
    It has the following fields:
    - user: a foreign key to the User model
    - name: the name of the doctor
    - specialty: the specialty of the doctor
    - experience: the experience of the doctor
    - phone_number: the phone number of the doctor
    - created_at: the date and time the doctor was created
    """

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor')
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    experience = models.IntegerField()
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Doctor'
        verbose_name_plural = 'Doctors'
        ordering = ['created_at']
    
    def __str__(self):
        return f"Dr. {self.name} is a {self.specialty} with {self.experience} years of experience."
