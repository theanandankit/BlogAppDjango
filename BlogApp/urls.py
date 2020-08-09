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
    url(r'^api/follow-list/$',FollowView.as_view(),name='profile_list'),
    url(r'^api/following-list/$',FollowingView.as_view(),name='profile_list'),
    url(r'^api/start-follow/$',register_Follow.as_view(),name='profile_list'),
    url(r'^api/blog-info/$',BlogInfoView.as_view(),name='profile_list'),
    url(r'^api/create-group/$',CreateGroupView.as_view(),name='profile_list'),
    url(r'^api/join-group/$',JoinGroupView.as_view(),name='profile_list'),
    url(r'^api/group-info/$',GroupInfoView.as_view(),name='profile_list'),
    url(r'^api/full-profile-info/$',FullProfileInfoView.as_view(),name='profile_list'),
    url(r'^api/add-blog/$',BlogaddView.as_view(),name='profile_list'),
    url(r'^api/search-blog/$',BlogSearchView.as_view(),name='profile_list'),
    url(r'^api/search-profile/$',ProfileSearchView.as_view(),name='profile_list'),
    url(r'^api/get-categories/$',GetCategoryView.as_view(),name='profile_list'),
    url(r'^api/get-categories/$',GetCategoryView.as_view(),name='profile_list'),
    url(r'^api/get-created-groups/$',GetCreatedGroupsView.as_view(),name='profile_list'),
    url(r'^api/public-blog/$',publicBlogView.as_view(),name='profile_list'),
    url(r'^api/group-list/$',Grouplistview.as_view(),name='profile_list'),
    url(r'^api/group-blog/$',GroupsBlogView.as_view(),name='profile_list'),
]