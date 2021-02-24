# link\urls.py

from django.urls import path, re_path
from linkList import views
from linkList.models import LinkList
# from django.views.generic import TemplateView, ListView, DetailView

app_name = 'linkList'

urlpatterns = [

    # link
    path('', views.linkLV.as_view(), name='index'),  # /lnk/
    path('<int:pk>', views.linkDV.as_view(), name='link_detail'),
    # path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
    path('add/', views.linkCreateView.as_view(), name='add'),
    path('change/', views.linkChangeLV.as_view(), name='change'),
    path('<int:pk>/update/', views.linkUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.linkDeleteView.as_view(), name='delete'),

    # # TAG
    path('tag/', views.TagCloudTV.as_view(), name='tag_cloud'),  # /lnk/tag/
    path('tag/<str:tag>/', views.TaggedObjectLV.as_view(), name='tagged_object_list'),  # /blog/tag/tagname/

]

