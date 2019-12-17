from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=254, default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=10, default='')
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, default=None)
    
    def __str__(self):
        return self.name