from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'first_name',
            'last_name',
            'street_address',
            'city',
            'state',
            'postal_code',
            'country',
            'phone_number',
            'date_of_birth',
        )

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'street_address',
            'city',
            'state',
            'postal_code',
            'country',
            'phone_number',
            'date_of_birth',
        )