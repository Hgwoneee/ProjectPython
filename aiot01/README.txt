1. DB(MySQL) 설정
-- root 계정으로 설정
create database aiot default character set utf8;
create user 'aiot'@'localhost' identified by 'aiot';
grant all privileges on aiot.* to 'aiot'@'localhost';
create user 'aiot'@'%' identified by 'aiot';
grant all privileges on aiot.* to 'aiot'@'%';

2. 마이그레이션 설정
python manage.py makemigrations
python manage.py migrate


3. python library 설치
명령 프롬프트(cmd)에서 아래 명령어를 실행시킨다.
pip install mysqlclient
pip install mysql.connector
pip install Django==3.2.19
pip install djangorestframework
pip install django-cors-headers


4.DB Migration
python manage.py makemigrations
python manage.py migrate


5. 공공데이터 수집
python manage.py fetchchargingstations


6. cors 설정
INSTALLED_APPS = [
    # ...
    'corsheaders',
    # ...
]

# 미들웨어 설정
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', 상단에 작성
    # ...
]

CORS_ALLOW_ALL_ORIGINS = True 모든 도메인 허용


7. django 실행
python manage.py runserver 0.0.0.0:8000

