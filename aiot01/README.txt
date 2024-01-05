1. DB(MySQL) 설정
-- root 계정으로 설정
create database aiot default character set utf8;
create user 'aiot'@'localhost' identified by 'aiot';
grant all privileges on aiot.* to 'aiot'@'localhost';
create user 'aiot'@'%' identified by 'aiot';
grant all privileges on aiot.* to 'aiot'@'%';

2. 공공데이터 수집
python manage.py fetchchargingstations

3. django 실행
python manage.py runserver 0.0.0.0:8000

