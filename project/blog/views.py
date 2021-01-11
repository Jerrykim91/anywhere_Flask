
# Create your views here.

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# 로그인 

from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as login
from django.contrib.auth import logout as logout
from django.contrib.auth import get_user_model

# 클래스형 제네릭뷰

from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

# comment
from django.conf import settings

# 테이블 조회를 위한 모델 임포트
from blog.models import Post


# import datetime
# now = datetime.datetime.now()

from django.views.generic import TemplateView

# TemplateView
class HomeView(TemplateView):
    """
    docstring
    """
    template_name = 'blog/home.html'

#ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

# DetailView
class PostDV(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}"
        context['disqus_id'] = f"post-{self.object.id}-{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

# ArchiveView
class PostAV(ArchiveIndexView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'
    make_object_list = True

class PostMAV(MonthArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

class PostDAV(DayArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    """
    docstring
    """
    model = Post
    date_field = 'modify_dt'


# TAG

class TagCloudTV(TemplateView):
    """
    docstring
    """
    template_name = 'blog/taggit/taggit_cloud.html'


class TaggedObjectLV(ListView):
    """
    docstring
    """
    template_name = 'blog/taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        """
        docstring
        """
        return Post.objects.filter(tags__name= self.kwargs.get('tag'))


    def get_context_data(self, **kwargs):
        """
        docstring
        """
        context = super().get_context_data(**kwargs)    
        context['tagname'] = self.kwargs['tag']
        return context

"""
https://velog.io/@hwang-eunji/django-views-%ED%95%A8%EC%88%98%ED%98%95-vs-%ED%81%B4%EB%9E%98%EC%8A%A4%ED%98%95-%EC%A0%9C%EB%84%A4%EB%A6%AD
"""


# db
# from django.db import connection
# cursor = connection.cursor()
# from .models import join # 모델 호출 
# User = get_user_model() # 변수 선언

# Create your views here.

# context = {
#         "PageName":PageName, 
#         'test':' 테스트 - 한국어'
#         }


# # @csrf_exempt
# def test(request):
#     '''
#     test - 글쓰기
#     '''
#     if request.method == 'GET':
#         return render(request,'blog/test.html')


# # @csrf_exempt
# def blog(request):
#     '''
#     blog - blogs
#     post -> blog single
#     # 여기서부터 골머리 시작 
#     '''
#     if request.method == 'GET':
#         return render(request,'blog/blog.html')


# # @csrf_exempt
# def posting(request):
#     '''
#     posting 
#     post -> blog single
#     # 여기서부터 골머리 시작 
#     '''
#     if request.method == 'GET':
#         return render(request,'blog/blog-single.html')


# # @csrf_exempt
# def about_me(request):
#     '''
#     about_me - 나에 대해서 
#     '''
#     if request.method == 'GET':
#         return render(request,'blog/about.html')


# # @csrf_exempt
# def main(request):
#     '''
#     main - 블로그 메인
#     '''
#     if request.method == 'GET':
#         return render(request,'blog/index.html')

# @csrf_exempt
# def test(request):
#     '''
#     test - counselor
#     '''
#     if request.method == 'GET':
#         PageName='test'
#         return render(request,'blog/counselor.html',{"PageName":PageName})


# @csrf_exempt
# def blog(request):
#     '''
#     blog - blogs
#     post -> blog single
#     # 여기서부터 골머리 시작 
#     '''
#     if request.method == 'GET':
#         PageName='blog'
#         return render(request,'blog/blog.html',{"PageName":PageName})


# @csrf_exempt
# def posting(request):
#     '''
#     posting 
#     post -> blog single
#     # 여기서부터 골머리 시작 
#     '''
#     if request.method == 'GET':
#         PageName='post'
#         return render(request,'blog/blog-single.html', {"PageName":PageName})


# @csrf_exempt
# def about_me(request):
#     '''
#     about_me - 나에 대해서 
#     '''
#     if request.method == 'GET':
#         PageName='about'
       
#         return render(request,'blog/about.html',{"PageName":PageName})


# @csrf_exempt
# def main(request):
#     '''
#     main - 블로그 메인
#     '''
#     if request.method == 'GET':
#         return render(request,'blog/index.html')