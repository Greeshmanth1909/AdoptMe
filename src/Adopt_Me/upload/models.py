from django.db import models
from django.forms import ModelForm
# Create your models here.

class upload_img(models.Model):
    animal = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images')
    description = models.CharField(max_length=200)
