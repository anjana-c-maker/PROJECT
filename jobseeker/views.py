from django.contrib import messages
from multiprocessing import context
from django.shortcuts import redirect,render
from .models import Jobseeker, Resume
from .forms import CreateProfile, CreateResume
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required
def profile_view(request,pk) :
    print(pk)
    jobseeker = Jobseeker.objects.get(id=pk)
    context={"jobseeker":jobseeker}
    print(jobseeker)
    return render(request,"jobseeker/profile.html",context)




@login_required   
def profile_create(request):
    form = CreateProfile()
    if request.method == "POST":
        form = CreateProfile(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            print('created profile')
    context ={
        "form": form
    }
    messages.success(request, 'Profile has been created.')
    return render(request,"jobseeker/createprofile.html",context)




@login_required   
def profile_update(request,pk):
    jobseeker=Jobseeker.objects.get(id=pk)
    form = CreateProfile()
    if request.method =="POST" :
        form = CreateProfile(request.POST,request.FILES,instance=jobseeker)
        if form.is_valid():
            form.save()
            print('Profile Updated')
    context={
        "jobseeker":jobseeker,
        "form": form
         }
    messages.success(request, 'Your profile was updated.')     
    return render(request,"jobseeker/updateprofile.html",context)     





@login_required   
def profile_delete(request,pk):
    jobseeker=Jobseeker.objects.get(id=pk)
    jobseeker.delete()
    print("Successfully deleted")
    messages.error(request, 'Document deleted.')
    return redirect("/jobseeker")





@login_required   
def resume_create(request):
    form = CreateResume()
    if request.method == "POST":
        form = CreateResume(request.POST)
        if form.is_valid():
            form.save()
            print('created resume')
    context ={
        "form": form
    }
    return render(request,"jobseeker/accept_resume.html",context)




def JsLandingpage(request) :
    return render(request,"jobseeker/jslandingpage.html")



                 




  
