from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Mandatory email field
    phone_number = models.CharField(max_length=20, blank=True)  # Optional phone number
    street_address = models.CharField(max_length=255, blank=True)  # Optional street address
    account_name = models.CharField(max_length=255, blank=True)  # Optional account name
    country = models.CharField(max_length=100, blank=True)  # Optional country

    def __str__(self):
        return self.username