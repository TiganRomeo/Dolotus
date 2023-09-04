from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, EmailAuthenticationForm
from django.urls import reverse_lazy

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the homepage after registration
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = EmailAuthenticationForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
