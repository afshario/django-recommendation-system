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
      
class Article(models.Model):
      '''
      Article model
      '''
      author = models.ForeignKey(User,on_delete=models.CASCADE ,related_name="articles")
      title = models.CharField(max_length=255)
      content = models.TextField()
      uvotec = models.PositiveIntegerField(default=0)
      dvotec = models.PositiveIntegerField(default=0)
      tags = models.ManyToManyField('Tag', related_name="articles")
      is_open = models.BooleanField(default=True)
      published = models.BooleanField(default=False)