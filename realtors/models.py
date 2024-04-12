from django.db import models
from datetime import datetime
# Create your models here.

class Realtors(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='images/realtors/')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    top_seller = models.BooleanField(default=False)
    date_hired = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
        return self.name