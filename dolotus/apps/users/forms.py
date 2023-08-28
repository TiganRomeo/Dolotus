from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    # Add any additional fields you want to include in the registration form
    phone_number = forms.CharField(max_length=20, required=False)
    street_address = forms.CharField(max_length=255, required=False)
    account_name = forms.CharField(max_length=255, required=False)
    country = forms.CharField(max_length=100, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'street_address', 'account_name', 'country')