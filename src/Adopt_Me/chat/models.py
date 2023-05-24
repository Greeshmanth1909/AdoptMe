from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# sender receiver message time and date 
class DirectMessages(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)
    message = models.TextField()
    time = models.TimeField()
    date = models.DateField()

