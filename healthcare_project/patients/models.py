from django.db import models
from django.conf import settings

# Create your models here.
class Patient(models.Model):
    """
    This is the model for the patient
    """
    user: models.ForeignKey = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='patients')
    age: models.IntegerField = models
    address: models.CharField = models.CharField(max_length=255)
    phone_number: models.CharField = models.CharField(max_length=20)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)