# blog\urls.py

from django.urls import path, re_path
from photo import views
from django.views.generic import TemplateView

app_name = 'photo'

urlpatterns = [

    # photo
    path('', views.AlbumLV.as_view(), name='index'),
    path('album', views.AlbumLV.as_view(), name='album_list'),
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),


    # App Extend
    path('album/add/', views.AlbumCV.as_view(), name='album_add'),
    path('album/change/', views.AlbumChLV.as_view(), name='album_change'),
    path('album/<int:pk>/update/', views.AlbumUV.as_view(), name='album_update'),
    path('album/<int:pk>/delete/', views.AlbumDelV.as_view(), name='album_delete'),


    path('add/', views.PhotoCV.as_view(), name='photo_add'),
    path('change/', views.PhotoChLV.as_view(), name='photo_change'),
    path('<int:pk>/update/', views.PhotoUV.as_view(), name='photo_update'),
    path('<int:pk>/delete/', views.PhotoDelV.as_view(), name='photo_delete'),


]
