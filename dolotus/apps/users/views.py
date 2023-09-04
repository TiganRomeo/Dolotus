from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomUserChangeForm, CustomUserCreationForm

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'You have successfully registered and logged in.')
            return redirect('home')  # Redirect to the homepage after registration
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # Redirect to the homepage after login
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')
    return render(request, 'user/login.html')

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Profile update failed. Please correct the errors.')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'user/profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important for maintaining user login state
            messages.success(request, 'Password changed successfully.')
            return redirect('user_profile')
        else:
            messages.error(request, 'Password change failed. Please correct the errors.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/password_change.html', {'form': form})