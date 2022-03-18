from django.urls import path
from.import views
from .views import *

app_name = "jobseeker"

urlpatterns = [
    path('<int:pk>/',profile_view, name='profile-view'),
    path('<int:pk>/update',profile_update,  name='profile-update'),
    path('<int:pk>/delete',profile_delete,  name='profile-delete'),
    path('create/',profile_create,  name='profile-create'),
    path('resume/',resume_create,  name='resume-create'),
    path('',views.JsLandingpage,  name='jslandingpage'),
]
