
from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Jobseeker, Resume

class CreateProfile(forms.ModelForm) :
    class Meta:
        model = Jobseeker
        fields = '__all__'


class CreateResume(forms.ModelForm) :
    class Meta:
        model = Resume
        fields = '__all__'


       