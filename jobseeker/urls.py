from re import search
from django.urls import path
from.import views
from .views import *

app_name = "jobseeker"

urlpatterns = [
    path('<int:pk>/',profile_view, name='profile-view'),
    path('<int:pk>/update',profile_update,  name='profile-update'),
    path('<int:pk>/delete',profile_delete,  name='profile-delete'),
    path('create/',profile_create,  name='profile-create'),
    path('<int:pk>/resumeview',resume_view,  name='resume-view'),
    path('resume/',resume_create,  name='resume-create'),
    path("resumelist/", views.ResumeList.as_view(), name="resume-list"),
    path('',views.JsLandingpage,  name='jslandingpage'),
    path("bloglist/", views.BlogPostList.as_view(), name="blog-post-list"),
    path("<int:pk>/viewblogs/", views.blog_view, name="blog-post-view"),
    path("<int:pk>/updateblog/", views.UpdateBlog.as_view(), name="blog-update"),
    path("<int:pk>/deleteblog/", views.DeleteBlog.as_view(), name="blog-delete"),
    path("createblog/", views. BuildBlog.as_view(), name="blog-create"),
    path("career/", career, name="career"),
    path("about/", about, name="about"),
    path("search/", views.SearchView.as_view(), name="search"),
]
