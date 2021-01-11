# blog\urls.py

from django.urls import path, re_path
from blog import views 

app_name='blog'

urlpatterns = [

    ##################################################
       
    path('',views.PostLV.as_view(), name='index'), # /blog/
    path('post/',views.PostLV.as_view(), name='post_list'), # /blog/post/
    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), #/blog/post/???
    path('archive/', views.PostAV.as_view(), name='post_archive'), # /blog/archive/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'), # /blog/archive/2020
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'), # /blog/archive/2020/Dec
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'), # /blog/archive/2020/Dec/28
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'), # /blog/archive/today/

    # TAG
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'), # /blog/tag/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'), # /blog/tag/tagname/

]
