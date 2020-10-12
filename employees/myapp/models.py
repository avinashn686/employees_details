from django.db import models
from PIL import Image


class register(models.Model):
    empid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    image = models.ImageField(upload_to='static')
    address = models.CharField(max_length=75)
    phonenumber = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return (self.username)

    class Meta:
        db_table = 'register'
# Create your models here.
