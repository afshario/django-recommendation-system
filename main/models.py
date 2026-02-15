from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
      '''
      this is a class to define users for rec_system
      '''
      username = models.CharField(max_length=250,unique=True)
      email = models.EmailField(unique=True)
      is_active = models.BooleanField(default= False)
      is_staff = models.BooleanField(default= False)

      USERNAME_FIELD = "email"
      
