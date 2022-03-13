from django.db import models
from django.conf import settings
from manager.models import Trip
import random ,uuid
# Create your models here.

def f():
    d = uuid.uuid4()
    str = d.hex
    return str[0:4]

class Book(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    recet_number = models.CharField(max_length=18,default=f,unique=True)
    trip_id = models.ForeignKey(Trip,related_name='Trip',on_delete=models.CASCADE)
    status = models.CharField(max_length=10 , default="pending" )
    date_published = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_published']
    def __str__(self):
        return self.author.username

