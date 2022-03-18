from django.db import models
from django.contrib.auth.models import AbstractUser

'''class Type(models.Model):
    USER_CHOICES = (
        ('Jobseeker','Jobseeker'),
        ('Employer','Employer'),
    )
    type = models.CharField(choices=USER_CHOICES, max_length=200)


    def __str__(self):
        return f"{self.name}"
      

  '''

class User(AbstractUser):
    USER_CHOICES = (
        ('Jobseeker','Jobseeker'),
        ('Employer','Employer'),
    )
    type = models.CharField(choices=USER_CHOICES, max_length=200)
     
    def __str__(self):
     return f"{self.first_name}.{self.last_name}"


 
      
