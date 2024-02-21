from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


# Create your models here.
class Image(models.Model):
    photo=models.ImageField(upload_to="myimage")
    date=models.DateTimeField(auto_now_add=True)



class Contact(models.Model):
    name = models.CharField( max_length=100)
    email = models.EmailField( max_length=100)
    message = models.CharField(max_length=200)