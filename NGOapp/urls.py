"""
URL configuration for NGOpro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from .views import *

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', home , name='home'),
    path('Aboutus',about ,name='about'),
    path('work' , work , name='work'),
    path('project' , project , name='project'),
    path('media' , media , name='media'),
    path('get' , get , name='get'),
    path('blog', blog , name='blog'),
    path('volunteer/', volunteer_signup, name='volunteer_signup'),
    path('volunteers/', volunteer_list, name='volunteer_list'),
    path('volunteers/', volunteer_list, name='volunteer_list'),
    path('donate/', donate, name='donate'),
    path('school/',schooldrive , name='schooldrive'),
    path('womenhealth',womenhealth , name='womenhealth'),
    path('download_report/', download_report, name='download_report'),
    path('download_skill_report/', download_skill_report, name='download_skill_report'),
    path('download_health_report/', download_health_report, name='download_health_report'),
    path('empowerwomen' , empowerwomen , name='empowerwomen'),
    path('edumilestone' , edumilestone , name='edumilestone'),
    path('healthcare' , healthcare , name='healthcare'),
    path('schoolinbox' , schoolinbox , name='schoolinbox'),
    path('login/', login_view, name='login'),
    path('register/', register_view , name='register'),
    path('logout/', logout_view, name='logout'),
]
