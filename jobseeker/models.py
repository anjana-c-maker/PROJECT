from distutils.command.upload import upload
import email
from pickle import TRUE
from random import choices
from unicodedata import name
from django.db import models
from django.forms import BooleanField

class Jobseeker(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age=models.IntegerField(default=0)
    GENDER =(
        ('male','Male'),
        ('female','Female'),
    )
    Gender = models.CharField(choices = GENDER, max_length=50)
    permanent_address = models.TextField()
    phone_number =models.IntegerField()
    profile_picture = models.ImageField(blank=True, null=True,upload_to='static/imgaes')
    education_details = models.TextField()
    fresher=models.BooleanField(default=False)
    dob=models.DateField( auto_now_add=True)
    special_files = models.FileField(blank=True, null=True)
    
    def __str__(self) :
        return f"{self.first_name} {self.last_name}"


class Resume(models.Model) :
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    education = models.TextField(max_length=1000) 
    skills = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000)
    about =  models.TextField(max_length=1000)

    def __str__(self):
        return f"{self.name}"
  
