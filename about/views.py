from django.shortcuts import render
from .models import Education


def about(request):
    educations = Education.objects.all()
    return render(request, 'about/about.html', {'educations': educations})
