
from django import forms
from .models import Jobseeker, Resume,BlogPost

class CreateProfile(forms.ModelForm) :
    class Meta:
        model = Jobseeker
        fields = ('first_name','last_name','age','Gender','permanent_address','phone_number','profile_picture','education_details','fresher','dob','special_files')


class CreateResume(forms.ModelForm) :
    class Meta:
        model = Resume
        fields = ('name','email','phone','address','summary','education','skills','experience','about','certifications')


class CreateBlog(forms.ModelForm) :
    class Meta:
        model = BlogPost
        fields = '__all__'        


       