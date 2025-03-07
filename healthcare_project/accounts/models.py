from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    """
    This is the model for the user
    """
    email: models.EmailField = models.EmailField(unique=True)
    name: models.CharField = models.CharField(max_length=255)
    password: models.CharField = models.CharField(max_length=255)
