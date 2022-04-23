
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Jobseeker(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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
    dob=models.DateField()
    special_files = models.FileField(blank=True, null=True)
    
    def __str__(self) :
        return f"{self.first_name} {self.last_name}"


class Resume(models.Model) :
    name = models.CharField(max_length=100)
    summary =models.CharField(max_length=255,default='')
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    address = models.TextField(max_length=1000)
    education = models.TextField(max_length=1000) 
    skills = models.TextField(max_length=1000)
    experience = models.TextField(max_length=1000)
    about =  models.TextField(max_length=1000)
    certifications =models.CharField(max_length=255,default='')

    def __str__(self):
        return f"{self.name}"
  
class BlogPost(models.Model) :
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255) 
    body =models.TextField()

    def __str__(self):
        return f"{self.title} + '|' +{self.author} "