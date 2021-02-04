from django.db import models
from django.contrib.auth.models import User
User._meta.get_field('email')._unique = True
from datetime import datetime


# Create your models here.

class Contact(models.Model):
    username = models.CharField( max_length=50)
    email    = models.EmailField( max_length=50)
    contact  = models.CharField( max_length=12)
    password = models.CharField( max_length=20)
    date     = models.DateField()

# below fn gives a user  name in database rather than info1 info2 
    def __str__(self):
        return self.username
        # return delf.email
        # return self.desc    any member of class whatever we want to show 

# for uploading images 
class FilesAdmin(models.Model):
    adminupload=models.FileField(upload_to='media')
    title      =models.CharField(max_length=50)

    def __str__(self):
        return self.title