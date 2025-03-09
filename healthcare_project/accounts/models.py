# healthcare_project/accounts/models
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class User(AbstractUser):
    """
    This is the model for the user
    """
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)

    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    is_admin_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        # db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
    
    def __str__(self):
        return f"{self.name} - {self.email} is {'a patient' if self.is_patient else 'a doctor' if self.is_doctor else 'an admin staff member' if self.is_admin_staff else 'a user'}"
