from django.urls import path, re_path
from blog import views 
from blog.models import Post

app_name='blog'

urlpatterns = [

    ##################################################

    # BLOG  
    path('',views.PostLV.as_view(), name='index'), # /blog/
    path('post/',views.PostLV.as_view(), name='post_list'), # /blog/post/
    # path('post/',views.PostLV.as_view(), name='post_list'), # /blog/post/
    # re_path(r'^category/(?P<hierarchy>[-\w]+)/^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), #/blog/post/???

    re_path(r'^post/(?P<slug>[-\w]+)/$', views.PostDV.as_view(), name='post_detail'), #/blog/post/???
    path('archive/', views.PostAV.as_view(), name='post_archive'), # /blog/archive/
    path('archive/<int:year>/', views.PostYAV.as_view(), name='post_year_archive'), # /blog/archive/2020
    path('archive/<int:year>/<str:month>/', views.PostMAV.as_view(), name='post_month_archive'), # /blog/archive/2020/Dec
    path('archive/<int:year>/<str:month>/<int:day>/', views.PostDAV.as_view(), name='post_day_archive'), # /blog/archive/2020/Dec/28
    path('archive/today/', views.PostTAV.as_view(), name='post_today_archive'), # /blog/archive/today/

    # App Extend
    path('add/', views.PostCreateView.as_view(), name='add'),
    path('change/', views.PostChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='delete'),


    # TAG
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'), # /blog/tag/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'), # /blog/tag/tagname/

    # Search
    path('search/', views.SearchFormView.as_view(), name='search'),

    # aboutmE
    path('about/', views.AboutDV.as_view(), name='post_about'), # /blog/about/

    # category
    path('addCategory/',views.addCategoryView.as_view(), name='add_category'), # /blog/addCategory/
    path('<str:cats>/',views.CategoryView, name='category'), # /blog/category_name/
    # re_path(r'^post/(?P<str:cats>[-\w]+/$', views.CategoryView, name='category'),

]
