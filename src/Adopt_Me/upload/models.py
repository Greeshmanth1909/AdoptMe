from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
# Create your models here.

class upload_img(models.Model):
    dateTime = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    animal = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images')
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    adopted = models.BooleanField(default=False)