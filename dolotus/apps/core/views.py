from django.shortcuts import render

def home(request):
    # Your homepage view logic here
    return render(request, 'home/home.html')