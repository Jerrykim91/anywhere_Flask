
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# 로그인 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as login
from django.contrib.auth import logout as logout
from django.contrib.auth import get_user_model


@csrf_exempt
def Main(request):
    '''
    Main 
    '''
    if request.method == 'GET':
        return render(request,'index_kr.html')

# db
# from django.db import connection
# cursor = connection.cursor()
# from .models import join # 모델 호출 
# User = get_user_model() # 변수 선언

# Create your views here.

# txt = """

#     <html>
#     <head><title>%s</title></head>
#     <body>
#     <h1>%s</h1><p>%s</p>
#     </body>
#     </html>
#       """% (
# '제리 | test 진행중',
# '정상동작 합니다.',
# '다음 스탭으로 진행합니다!'
# )


# @csrf_exempt
# def Main(request):
#     '''
#     테스트 버전 Dummy
#     '''
#     return HttpResponse(txt)

