from django.shortcuts import render

def Landing_page(request) :
    return render(request,"employer/eplandingpage.html")
