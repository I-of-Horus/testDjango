from django.db import models

# Create your models here.
from django.conf import settings
from django.db import models
from django.utils import timezone
"""
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
"""
class Post_footballer(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    footballer_name = models.CharField(max_length=100, default="default name")
    footballer_curr_club  = models.CharField(max_length=100, default="default clubname")
  
    created_date = models.DateTimeField(default=timezone.now)
    last_mod_date = models.DateTimeField(blank=True, null=True)
    published_date = models.DateTimeField(blank=True, null=True)


def publish(self):
   self.published_date = timezone.now()
   self.save()

def __str__(self):
    return self.title