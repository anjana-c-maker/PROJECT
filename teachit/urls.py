
from django import views
from django import urls
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from accounts.views import*
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page ,name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('jobseeker/', include('jobseeker.urls', namespace='jobseeker')),
    path('employer/', include('employer.urls', namespace='employer')),
]

if settings.DEBUG :
    urlpatterns += static(settings.STATIC_URL, documnet_root=settings.STATIC_ROOT) 
