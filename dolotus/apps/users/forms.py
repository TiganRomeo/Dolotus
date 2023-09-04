from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'street_address', 'city', 'state', 'postal_code', 'country', 'phone_number', 'date_of_birth')
