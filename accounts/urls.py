
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView


app_name = "accounts"

urlpatterns = [
    path('home/',views.home_page , name='homepage'),
    path('register/',views.register , name='register'),
    path('login/',views.CustomLoginView.as_view() , name='login'),
    path("logout/", views.LogoutView.as_view(), name="logout"),

]


