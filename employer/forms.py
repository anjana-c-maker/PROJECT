
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Employer, JobPost


class CreateProfile(forms.ModelForm) :
    class Meta:
        model = Employer
        fields = ('first_name','last_name','email_address','phone_number','school_name','designation','address','city','skills_hire_for','exprience_inhiring','level')


class BuildJobPost(forms.ModelForm) :
    class Meta:
        model = JobPost
        fields = '__all__'        
