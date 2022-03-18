from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import *

User = get_user_model()

class CustomUserForm(UserCreationForm) :
    '''class Meta :
        model = Type
        fields = '__all__'
    '''  
    class Meta :
        model = User
        fields =('username','password1','password2','email','first_name','last_name', 'type')




