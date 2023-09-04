from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('register/', views.user_register, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]
