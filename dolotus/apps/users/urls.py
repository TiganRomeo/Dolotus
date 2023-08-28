from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = 'users'  # Set an app namespace if desired

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', views.user_profile, name='user_profile'),
]