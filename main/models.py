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


class Tag(models.Model):
      title = models.CharField(max_length=255)

class Comment(models.Model):
      author = models.ForeignKey(User,on_delete=models.CASCADE)
      content = models.TextField(max_length= 400)
      article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
      class Meta:
            unique_together = ('author', 'article')

class Vote(models.Model):
      VOTE_TYPES = (
            ('up', 'Upvote'),
            ('down', 'Downvote'),
      )
      voter = models.ForeignKey(User,on_delete=models.CASCADE,related_name= 'votes')
      article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name= 'articles')
      type = models.CharField(max_length=4, choices=VOTE_TYPES)
      class Meta:
            unique_together = ('voter', 'article')
