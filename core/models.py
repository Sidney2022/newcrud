from dataclasses import field
from tkinter import CASCADE
from tkinter.messagebox import NO
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
User = get_user_model()
# Create your models here.
class Post(models.Model):
       user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
       title = models.CharField(max_length=100)
       description = models.TextField()
       date_added = models.DateTimeField(default=timezone.now)
       
       def __str__(self) -> str:
              return self.title
       
       
class Profile(models.Model):
       first_name = models.CharField(max_length=50, default=None)
       last_name = models.CharField(max_length=50, default=None)
       username = models.CharField(max_length=50)
       email = models.EmailField()
       password = models.CharField(max_length=50)

       def __str__(self) -> str:
              return self.username