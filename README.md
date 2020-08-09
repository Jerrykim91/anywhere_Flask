# portfolio - Test Ver 

<br>

## 1차 - 배포(deployment)테스트

기본적으로 장고 세팅은 혼자 할 수 있다는 가정하에 진행한다.

##### 실제로는 3번째 테스트 

git 이 있으면 그냥 진행 없으면 설치 작업 진행 

- `git add` , `git add --all` : 추가      
- `git status` : 스테이지 된 파일, 브랜치상태 등의 정보를 보여줌 
- `git commit -m "first commit"` : 커밋 메세지 작성과 동시에 커밋

- `git push -u origin master` : 푸쉬
<br>
<br>

## [PythonAnywhere](www.pythonanywhere.com) 에 가입 

<br>

초보자로 회원가입 -> 3개월동안만 서버를 열어놓는것이 유효     

이후에는 결제해야하는것 같았다.      

그러니 생각해보고 하는것을 추천! 일단은 편해서 .... 이걸로 진행 ! 

<br>

## 네비바에 콘솔(`Consoles`)창 이동

가입할때 사용한 내 아이디가 주소가 된다. 

가입하면 상단에 네비바에 콘솔(Consoles)창을 확인가능하다 

거기서 기본세팅을 할것이다. 

<br>

콘솔창을 띄운후 

하원4131
이메일 : 서브이메일 -> jerrykim91
비번 지은 4131
```bash
git clone 주소.git 
```

<br>

입력해주고 레퍼지토리가 잘 받아졌는지 tree를 통해서 확인해 본다. `$ tree 폴더이름`

가상환경을 추가할건데 bash Consoles에서 내 폴더로 이동한 다음 `$ cd 폴더`  

가상환경을 만든다. `$ virtualenv --python=python버.전 가상환경이름`

가상환경을 활성화 시킨다. `$ source 가상환경이름/bin/activate` or `workon 가상환경이름`

중간중간 패키지 설치하고 `pip install 모듈`

`$ python manage.py ckeck` 

데이터베이스 초기화 `$ python manage.py migrate` 

잊지말고 `(가상환경이름) $ python manage.py createsuperuser`  -> mysql은 초기에 설정해줘야함 ... (이거때문에 한번 밀어버린건 ... )


정적파일 수집( 서버가 찾을 수 있는 장소에 집합 ) `python manage.py collectstatic` -> 안될 경우 있음 그럴때는 일단 패스 

<br>

## 네비바 Web 창 이동 

Add a new web app 클릭한다.

그다음은 manual configuration 클릭한 후 파이썬 버전을 선택한다. (1차 세팅 완료) 

가상환경 경로를 설정해준다. 

<br>

## WSGI 설정 파일(WSGI configuration file) 설정 

<br>

참고로 장고 아님 PythonAnywhere Web 에서의 설정임 

```py

import os
import sys

path = '/home/아이디/폴더이름'  
# /home/jerrykim91/Portfolio/myenv/bin/python
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '설정폴더이름(=폴더이름).settings' # 에러발생 

from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())

```

<br>

## Static files 설정 

본인의 경로에 맞게 정해서 해주는것이 포인트 !!! 


| URL |	Directory	|
|:----:|:----------------------------------------:|
|`/static/`|`/home/아이디/폴더이름/static`|
|`/templates/`|`/home/아이디/폴더이름/templates`|

<br>

일단 완료 -> 템플릿 설정 없이 성공 

<br>
<br>

## 데이터 베이스 설정 하기 

<br>

MySQL 이기 때문에 모듈 설치를 하고 -> `pip install mysqlclient `

장고폴더.setting.py 에 들어가서 데이터 베이스 설정을 진행한다.


```py

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {

    # 초기설정
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    #     }

    # mysql
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '유저계정이름$데이터베이스이름',
        'USER': '유저계정이름',
        'PASSWORD': '데이터 베이스 생성시 PW',
        'HOST': '유저계정이름.mysql.pythonanywhere-services.com' # 데이터 베이스 생성하면 주는 호스트이름 ,
    }

    # mysql 가이드 
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'NAME': '<your_username>$<your_database_name>',
    #         'USER': '<your_username>',
    #         'PASSWORD': '<your_mysql_password>',
    #         'HOST': '<your_mysql_hostname>',
    #           }
}

```


여기서 잊지말고 `http://사용자id.pythonanywhere.com/admin/` 테스트 해보기 바람 .... 

<br>
<br>

## SECRET_KEY 의 보안을 위한 재설정 


(추후)

---

## 에러 발생 

작업 진행중 발생한 에러 

<br>

### [에러발생] 1. `python manage.py check ` or `python manage.py makemigrations` 를 진행했는데 아래와 같은 애러발생

[참고링크](https://stackoverflow.com/questions/49189402/auth-user-groups-fields-e304-reverse-accessor-for-user-groups-clashes-with)

<br>

```py

SystemCheckError: System check identified some issues:
ERRORS:
ToyMain.join.groups: (fields.E304) Reverse accessor for 'modelsClassName.groups' clashes with reverse accessor for 'User.groups'.
        HINT: Add or change a related_name argument to the definition for 'modelsClassName.groups' or 'User.groups'.
ToyMain.join.user_permissions: (fields.E304) Reverse accessor for 'modelsClassName.user_permissions' clashes with reverse accessor for 'User.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'modelsClassName.user_permissions' or 'User.user_permissions'.
auth.User.groups: (fields.E304) Reverse accessor for 'User.groups' clashes with reverse accessor for 'modelsClassName.groups'.
        HINT: Add or change a related_name argument to the definition for 'User.groups' or 'modelsClassName.groups'.
auth.User.user_permissions: (fields.E304) Reverse accessor for 'User.user_permissions' clashes with reverse accessor for 'modelsClassName.user_permissions'.
        HINT: Add or change a related_name argument to the definition for 'User.user_permissions' or 'modelsClassName.user_permissions'.


# [해결] 만약 모델을 만든다면 만든 모델 명시!!! -> 아니면 에러발생 
# AUTH_USER_MODEL = 'YourAppName.modelsClassName'

```

<br>

### [에러발생] 2. Strict Mode가 데이터베이스 연결 'default'에 대해 설정되지 않았습니다.

`python manage.py migrate ` 작업 수행 시 발생

[참고링크_1](https://stackoverflow.com/questions/23022858/force-strict-sql-mode-in-django)
[참고링크_2](https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode)

```py
(mysql.W002) MySQL Strict Mode is not set for database connection 'default'
        HINT: MySQL's Strict Mode fixes many data integrity problems in MySQL, such as data truncation upon insertion, by escalating warnings into errors. It is strongly recommended you activate it. See: https://docs.djangoproject.com/en/3.1/ref/databases/#mysql-sql-mode

# settings.py에서 Databases 항목에서 아래의 옵션 추가
DATABASES = { 
	...
	'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
             # 'sql_mode': 'traditional'
        },
```

<br>
<br>

---

#### 완료하기 전 에러 

이것 말고 기존에 있는 작업물로 진행하려다 하루를 날렸는데     

오늘 작업하다 확인한것이 Django 버전이 2.x 에서 3.x로 바뀌면서     
os 모듈을 이용하는 방식에서 path 모듈이용방식으로 바뀌었다. 

이부분을 재설정해주니까 탬플릿의 경로를 찾지 못하는 에러가 해결되었다(여기서만...)

이 프로젝트 같은경우 가상환경안에서 Django 프로젝트 폴더를 생성하고 한것이라 
기존에 있는 실패?한 프로젝트를 하나씩 엎어 가면서 오류를 찾아보고자 한다. 

역시 컴퓨터는 죄가 없다.... 내가 죄지... 모르는죄 크흡.....

하 4번째 밀기 .... ㅎㅎㅎㅎㅎㅎ 