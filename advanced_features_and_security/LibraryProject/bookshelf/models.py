from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager 

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField(default=2020)

    def __str__(self):
      return self.title
  
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()
    
    def __str__(self):
        return self.username
    

# Create your models here.
