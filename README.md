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
# /home/아이디/폴더이름/myenv/bin/python  #  내경로
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = '설정폴더이름(=폴더이름).settings' 

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

[참고](https://wayhome25.github.io/django/2017/07/11/django-settings-secret-key/)

프로젝트를 생성하면 장고의 `setting.py` 을 통해 여러가지 설정을하는데 거기서 가장 중요한것이 보안키(`SECRET_KEY`)

`SECRET_KEY` 장고 보안 기능에 활용되는 키 값으로 생각없이 내가 애용하는 github에 그대로 노출 ㅎㅎㅎㅎ 
몇번의 실패들..?을 해서 딱히 신경은 안썻지만 나..름..? 안정화 되고있어서 보안키를 노출하지 않는법을 공부했다. 


`SECRET_KEY` : 쿠키데이터, 해시, 암호화 같은 임시적인 일에 사용되며 변경 시 세션등의 데이터가 사라질수있다. 
                 50자의 랜덤 문자로 구성되어 있는데, Django Secret Key Generator 라는 것도 존재한다고 한다. 

용도 : 
- django.contrib.sessions.backends.cache 다른 세션 백엔드를 사용하거나       
    기본  get_session_auth_hash()를 사용하는 모든 세션
- CookieStorage 또는 FallbackStorage를 사용하는 모든 메시지
- 모든 PasswordResetView 토큰
- 다른 키가 제공되지 않는 암호화 서명사용

이뿐아니라 데이터베이스 정보 또한 보안을 고려해 관리하는 것이 좋다. 


### 키 분리하는 방법은 2가지가 있다. 

1. 환경변수 패턴
    - 환경 변수 -> ??? 
    - 환경변수를 사용하여 비밀 키를 보관함으로써 걱정 없이 세팅파일을 github 공개 저장소에 추가
    - `SECRET_KEY` 의 값을 환경변수에 저장하여 참고
    - 보통은 기업에서는 AWS 배포 시 환경변수로 등록해 배포 한다고한다. 

(조금더 공부한후에 작성)


2. 비밀파일 패턴

`.json` 파일을 만들어서 비밀 키를 저장하고 호출하여 사용한다. 

자 `secret.json` 의 이름으로 파일을 생성한다.

```json
// secret.json
{
    "SECRET_KEY"    : "b_4(!id8ro!1645n@ub55555hbu93gaia0 ",  //본인의 고유 비밀 키 추가
    "DATABASE_NAME" : "데이터 베이스 네임",
    "DATABASE_USER" : "유저 네임",
    "DATABASE_PASSWORD" : "패스워드"
}
```

나는 파일 형식으로 진행했다.
서버를 너무 잘 밀다보니 ..

```py
import json
from django.core.exceptions import ImproperlyConfigured

path = "secrets.json"
with open(path) as f:
    secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# SECRET_KEY 키 설정 
SECRET_KEY = get_secret("SECRET_KEY")

# DATABASES 키 설정 -> 디비 사용하는 사람만 설정
DATABASES = {
    'default': {
        ...
        'NAME': get_secret("DATABASE_NAME"),
        'USER': get_secret("DATABASE_USER"),
        'PASSWORD': get_secret("DATABASE_PASSWORD"),
        ...
    }
}
```
`secret.json` 는 제외하고 보안키는 개인적으로 관리하는것을 추천한다. 

이렇게 `secret.json`를 열심히 만들어 놓고 바보같이 공유 사이트나 github repo에 올리는 사람은 없겠지? 

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

### 한번 밀때마다의 후기

#### 1차 

기존에 만들어둔 프로젝트로 열려고 하니 
경로에러가 계속뜬다... 밀어야하나 ... 


#### 2차 

밀고 처음부터 했는데 
역시나 안된다... 무엇이 문제..인지 모르겠다... 
또 밀어서 다른 방법으로 접근해봐야지 ... 

#### 3차

다행이도 가상 환경안에서 Django 프로젝트 폴더를 생성하였더니 동작하였다. 

세팅부터 기존에 있는 실패?한 프로젝트를 하나씩 엎어 가면서 오류를 찾아보고자 한다. 

[ 템플릿 에러 해결]
작업하다 확인한것이 Django 버전이 2.x 에서 3.x로 바뀌면서     
os 모듈을 이용하는 방식에서 path 모듈 이용 방식으로 바뀌었다. 

이부분을 재설정해주니까 템플릿의 경로를 찾지 못하는 에러가 해결되었다. 
역시 컴퓨터는 죄가 없다.... 내가 죄지... 모르는죄 크흡... 항상 버전! 조심 


#### 4차

결국 밀고 새로 만들었다. 하 4번째 밀기 .... ㅎㅎㅎㅎㅎㅎ 
데이터 베이스(파이썬에니워어의db)를 장고 어플리케이션을 생성하고 만들엇더니 에러가났다.. 
버그라나 뭐라나...
슈퍼 계정에 접근하는데 에러가나서 설마했는데 몇시간을 헤매다가 결국 밀고 
지금은 ... 템플릿을 입힌 상태... 다행인데 왜 난 겁이나냐 ... 
앞으로가 걱정되는...ㅎㅎ