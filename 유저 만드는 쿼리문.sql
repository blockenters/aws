use mysql;
# python_user 라는 계정, 비밀번호 2105로 유저 생성하는 SQL
create user 'recipe_user'@'%' identified by '2105';

# 이 유저가 어떤 데이터베이스를 처리할수 있는지에 대한
# 권한 설정하는 SQL
# . 의 왼쪽 별표는 모든 데이터베이스 관리할수 있다는 뜻이고
# . 의 오른쪽 별표는 모든 테이블을 관리할수 있다는 뜻.
# yhdb.* 라고 썼다면, yhdb 의 모든 테이블을 관리할 수 있다는 뜻.
grant all on recipe_db.* to 'recipe_user'@'%';

