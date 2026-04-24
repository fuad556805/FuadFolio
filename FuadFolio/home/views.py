from django.shortcuts import render
from .models import Profile

def home(request):
    profile = Profile.objects.first()
    return render(request, 'home/home.html', {'profile': profile})