from django.urls import path
from . import views

app_name = 'users'  # Set an app namespace if desired

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
