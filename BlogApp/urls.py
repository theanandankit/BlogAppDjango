"""BlogApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from BlogAppapp1.views import *
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/register/$',register_new_user.as_view(),name='profile_list'),
    url(r'^api/change-password/$', ChangePasswordView.as_view(), name='profile_list'),
    url(r'^api/login/$',login.as_view(),name='profile_list'),
    url(r'^api/edit-profile/$',EditProfileView.as_view(),name='profile_list'),
    url(r'^api/get-profile/$',GetProfileView.as_view(),name='profile_list'),
    url(r'^api/get-user-info/$',GetUserInfoView.as_view(),name='profile_list'),
    url(r'^api/add-user-info/$',AddUserInfoView.as_view(),name='profile_list'),
<<<<<<< HEAD
    url(r'^api/follow-list/$',FollowView.as_view(),name='profile_list'),
    url(r'^api/following-list/$',FollowingView.as_view(),name='profile_list'),
    url(r'^api/start-follow/$',register_Follow.as_view(),name='profile_list'),
    url(r'^api/blog-info/$',BlogInfoView.as_view(),name='profile_list'),
=======
>>>>>>> d6825fdada2f612fe02d3fbe385363e232269888
    
]
    
