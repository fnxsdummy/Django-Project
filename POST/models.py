from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  img = models.ImageField(upload_to='media/')
  title = models.CharField(max_length=100)
  description = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return f'{self.user.username} || {self.title}'


class Message(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  message = models.CharField(max_length=400)
  created_at = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return f'{self.user.username} || {self.message}'