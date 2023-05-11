from django.db import models

# Create your models here.

class upload_img(models.Model):
    animal = models.CharField(max_length=15)
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=200)
