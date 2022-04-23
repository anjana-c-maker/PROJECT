from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserForm
from django.contrib.auth.views import LoginView,LogoutView


class CustomLoginView(LoginView):
    def get_success_url(self):
        if self.request.user.type == 'Employer':
            return '/employer'
        else:
            return '/jobseeker'
        return self.get_redirect_url() or self.get_default_redirect_url()
    

def home_page(request):
    return render(request,'home.html')

def register(request) :
    form = CustomUserForm()
    if request.method =='POST' :
        form = CustomUserForm(request.POST)
        if form.is_valid() :
            form.save()
            print('Successfully registered')
            return redirect('accounts:login')
    context = {'form':form}
    return render(request,'registration/register.html',context)


    



