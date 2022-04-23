from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .forms import CreateProfile,BuildJobPost

from employer.models import Employer, JobPost

def Landing_page(request) :
    return render(request,"employer/eplandingpage.html")



class Create_recruiter_profile(CreateView) :
    model = Employer
    form_class = CreateProfile
    template_name= 'employer/createprofile.html'
    QuerySet =Employer.objects.all()

    def get_success_url(self):
        return '/employer'






class BuildJobPost(CreateView) :
    model = JobPost
    form_class = BuildJobPost
    template_name= 'employer/jobpost.html'
    query_set =JobPost.objects.all() 

    def get_success_url(self):
      return '/employer'



class JobPostList(ListView) :
    model = JobPost
    template_name= "employer/joblist.html"
    query_set =JobPost.objects.all() 
    context_object_name = 'jobs'

#detailview
def job_view(request,pk):
    job =JobPost.objects.get(id=pk)
    print(pk)
    context={
        "job" :job
    }
    return render(request,"employer/jobview.html",context)