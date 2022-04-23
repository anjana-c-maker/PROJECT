from ast import Pass
from sre_constants import CATEGORY
from turtle import title
from django.conf import settings
from django.db import models

class Employer(models.Model) :
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address =models.EmailField(max_length = 254, unique=True ,default="")
    phone_number =models.IntegerField()
    school_name =models.CharField(max_length=255)
    designation =models.CharField(max_length=255)
    address = models.TextField()
    city =models.CharField(max_length=255)
    skills_hire_for=  models.TextField()
    EXPERIENCE = (
    ('0','Less Than 1 year'),
    ('1','1+ Year'),
    ('2','2+ Year'),
    ('3','3+ Year'),
    ('4','4+ Year'),
    ('5','5+ Year'),
    ('6','6+ Year'),
    ('7','7+ Year'),
    ('8','8+ Year'),
    ('9','9+ Year'),
    ('10','10+ Year'),
    )
    exprience_inhiring = models.CharField(choices=EXPERIENCE ,max_length=255)
    LEVEL_HIRE_FOR = (
    ('junior level','Junior Level'),
    ('mid level', 'Mid Level '),
    ('high level','High Level'),
    )
    level = models.CharField(choices=LEVEL_HIRE_FOR ,max_length=255)

    def __str__(self) :
        return f"{self.first_name} {self.last_name}"


class JobPost(models.Model) :
    job_title  =models.CharField(max_length=255 ,default='')
    location =models.CharField(max_length=255 ,default='')
    requirements = models.TextField( null=True)
    qualification = models.TextField()

    experience = models.TextField()
    JOB_TYPE = (
        ('full time','Full Time'),
        ('part time' ,'Part Time')

    )
    jobtype = models.CharField(choices=JOB_TYPE ,max_length=255)
    woking_time = models.CharField(max_length=200)
    schedule = models.CharField(max_length=200)
    language =models.CharField(max_length=255)
    application_deadline = models.DateField()
    scale_of_pay =models.CharField(max_length=255 ,default='')

    def __str__(self):
        return f"{self.job_title}"
  




