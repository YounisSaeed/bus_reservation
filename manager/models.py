from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

class Trip(models.Model):
    company_name = models.CharField(max_length=50)
    dest_from = models.CharField(max_length=50)
    dest_to = models.CharField(max_length=50)
    time_from = models.TimeField( auto_now=False, auto_now_add=False)
    time_to = models.TimeField( auto_now=False, auto_now_add=False)
    date_day = models.DateField(auto_now=False, auto_now_add=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    price = models.CharField( max_length=50,null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_published']
    
    def __str__(self):
        return self.company_name