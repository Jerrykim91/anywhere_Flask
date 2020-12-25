
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt

# 로그인 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import authenticate as auth
from django.contrib.auth import login as login
from django.contrib.auth import logout as logout
from django.contrib.auth import get_user_model

# Create your views here.


@csrf_exempt
def MainKr(request):
    '''
    MainKr - 기본값 
    '''
    if request.method == 'GET':
        return render(request,'index_kr.html')


# @csrf_exempt
# def MainEn(request):
#     '''
#     MainEn - 영어
#     '''
#     if request.method == 'GET':
#         return render(request,'index_en.html')


def GDP(request):
    """
    GDP
    """
    if request.method == 'GET':
        PageName='GDP'
        return render(request,'Base.html', {"PageName":PageName}) 


def Vegetable(request):
    """
    Vegetable amount prediction
    """
    if request.method == 'GET':
        PageName='Vegetable'
        
        return render(request,'Base.html', {"PageName":PageName, 'test':' 테스트 - 한국어'})


def Food(request):
    """
    음식 이미지 분석 -> 
    """
    if request.method == 'GET':
        PageName='Food'
        return render(request,'Base.html', {"PageName":PageName})


def PostCovid(request):
    """
    포스트 코로나
    """
    if request.method == 'GET':
        PageName='PostCovid'
        return render(request,'Base.html', {"PageName":PageName})








# db
# from django.db import connection
# cursor = connection.cursor()
# from .models import join # 모델 호출 
# User = get_user_model() # 변수 선언



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

