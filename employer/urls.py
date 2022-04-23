from django.urls import path
from . import views

app_name="employer"

urlpatterns = [
    path('',views.Landing_page , name='landingpage'),
    path("create/", views.Create_recruiter_profile.as_view(), name="profile-create"),
    path("jobpost/", views.BuildJobPost.as_view(), name="build-job-post"),
    path("findjobs/", views.JobPostList.as_view(), name="job-post-list"),
    path("<int:pk>/viewjob/", views.job_view, name="job-post-view"),
]
