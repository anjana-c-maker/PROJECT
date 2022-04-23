
from django.contrib import messages
from django.shortcuts import redirect,render,reverse
from .models import Jobseeker, Resume ,BlogPost
from django.core.mail import send_mail
from .forms import CreateProfile, CreateResume,CreateBlog
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from employer.models import JobPost



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
            form = form.save(commit=False)
            form.user = request.user
            print('created profile')
            return redirect('jobseeker:jslandingpage')
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
            return redirect('jobseeker:jslandingpage')
    context={
        "jobseeker":jobseeker,
        "form": form
    }    
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
            return redirect('jobseeker:jslandingpage')
    context ={
        "form": form
    }
    return render(request,"jobseeker/accept_resume.html",context)




def JsLandingpage(request) :
    profile = Jobseeker.objects.get(user=request.user)
    return render(request,"jobseeker/jslandingpage.html", {'profile': profile})





def resume_view(request,pk):
    resume = Resume.objects.get(id=pk)
    print(pk)
    context={
        "resume":resume
    }
    return render(request,"jobseeker/resume_pdf.html",context)                 




#resumelist which is visible to all school systems
class ResumeList(ListView) :
    model = Resume
    template_name= "jobseeker/resumelist.html"
    query_set =Resume.objects.all() 
    context_object_name = 'resumes'




#blog create
class BuildBlog(CreateView) :
    model =BlogPost
    form_class = CreateBlog
    template_name= 'jobseeker/createblog.html'
    query_set =BlogPost.objects.all() 

    def get_success_url(self):
      return reverse("jobseeker:blog-post-list")
 
#blog list 
class BlogPostList(ListView) :
    model = BlogPost
    template_name= "jobseeker/bloglist.html"
    query_set =BlogPost.objects.all() 
    context_object_name = 'blogs'

#detailview
def blog_view(request,pk):
    blog =BlogPost.objects.get(id=pk)
    print(pk)
    context={
        "blog" :blog
    }
    return render(request,"jobseeker/blogview.html",context)



#updateview

class UpdateBlog(UpdateView) :
    model =BlogPost
    template_name= 'jobseeker/updateblog.html'
    query_set =BlogPost.objects.all() 
    form_class = CreateBlog

    def get_success_url(self):
      return reverse("jobseeker:blog-post-list")


#delete blog

class DeleteBlog(DeleteView) :
    model =BlogPost
    template_name= 'jobseeker/deleteblog.html'
    query_set =BlogPost.objects.all() 
    def get_success_url(self):
      return reverse("jobseeker:blog-post-list")    


def career(request):
    return render(request,"jobseeker/career.html")

def about(request):
    return render(request,"jobseeker/about.html")

class SearchView(ListView):
    model = JobPost
    template_name = 'jobseeker/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       
       if query:
          postresult = JobPost.objects.filter(job_title=query)
          result = postresult
          print(result)
       else:
           result = None
       return result    

    