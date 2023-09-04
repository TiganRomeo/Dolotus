from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Required. 30 characters or fewer.')
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = CustomUser  # Replace with your user model
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')
