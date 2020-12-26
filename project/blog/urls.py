# blog\urls.py

from django.urls import path
from . import views 


# # 로그인 
# urlpatterns = [

#     # 로그인 기능 
#     # path('sign_up', views.sign_up),
#     # path('sign_in', views.sign_in),
#     # path('user_delete', views.user_delete),
#     # path('sign_out', views.sign_out),
# ]


# blog 
urlpatterns = [
    
    # path('main', views.main, name ='main' ), # main
    path('about', views.about_me, name ='about' ), # about
    path('blog', views.blog, name ='blog' ), # blog
    path('post', views.posting, name ='post' ), # post
    path('test', views.test, name ='test' ), # test

]

