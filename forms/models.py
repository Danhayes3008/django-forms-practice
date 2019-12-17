from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userDetails(models.Model):
    name = models.CharField(max_length=254, default='')
    gender = models.CharField(max_length=10, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name