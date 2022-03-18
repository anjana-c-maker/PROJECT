from django.urls import path
from . import views

app_name="employer"

urlpatterns = [
    path('',views.Landing_page , name='landingpage'),
]
