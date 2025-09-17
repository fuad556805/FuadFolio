from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('contact/', include('contact.urls')),
]
