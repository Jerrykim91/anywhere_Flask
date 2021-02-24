"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

# 추가
from django.conf.urls.static import static
from django.conf import settings

# from blog.views import HomeView
from project.views import HomeView
from project.views import UserCreateView, UserCreateDoneTV

 
urlpatterns = [
    path('admin/', admin.site.urls), # 관리자 계정

    # 인증 
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/',UserCreateView.as_view(), name='register' ),
    path('accounts/register/done/', UserCreateDoneTV.as_view(),name ='register_done'),

    # 커스텀
    path('', HomeView.as_view(), name='home'),
    path('blog/', include('blog.urls')), # blog
    path('photo/', include('photo.urls')), # blog
    path('lnk/', include('linkList.urls')), # linkList
    path('markdownx/', include('markdownx.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
