from django.db import models

class Profile(models.Model):
    photo = models.ImageField(upload_to='profile/')
    
    def __str__(self):
        return "Profile"