# MainField\urls.py

from django.urls import path
from . import views 

# MainField 
urlpatterns = [

    path('GDP', views.GDP, name ='GDP' ), # GDP
    path('Vegetable', views.Vegetable), # Vegetable
    path('Food', views.Food),  # Food
    path('PostCovid', views.PostCovid),  # PostCovid

]



# # 로그인 
# urlpatterns = [

#     # 로그인 기능 
#     # path('sign_up', views.sign_up),
#     # path('sign_in', views.sign_in),
#     # path('user_delete', views.user_delete),
#     # path('sign_out', views.sign_out)

# ]

