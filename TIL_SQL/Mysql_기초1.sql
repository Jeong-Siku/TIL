# 1) 데이터 베이스 생성
CREATE DATABASE test;

# 2) 데이터 베이스 확인
# SHOW DATABASES;

# 3) 데이터 베이스 사용
USE test;

# 4) 선택된 데이터 베이스 확인
# SELECT DATABASE ();

# 5) 테이블 생성(제약조건 없이)
CREATE TABLE user1(
	user_id INT,
    name VARCHAR(20),
    email VARCHAR(30),
    age INT(3),
    rdate DATE
);

# 6) 테이블 생성(제약조건 있음)
CREATE TABLE user2(
	user_id INT PRIMARY KEY AUTO_INCREMENT, # 입력하지 않아도 숫자가 자동으로 증가
    name VARCHAR(20) NOT NULL, # 중복은 가능하나 널값 허용 X
    email VARCHAR(30) UNIQUE NOT NULL, #중복과 널값 허용 X 
    age INT(3) DEFAULT 30, # 공백으로 해도 기본값 기입
    rdate TIMESTAMP DEFAULT now() # DATE는 년월일, TIMESTAMP는 시간
);

# 데이터베이스, 테이블 변경 - ALTER
# 7) 현재 선택된 데이터 베이스의 문자집합 확인
# SHOW VARIABLES LIKE 'character_set_database';

# 8) 데이터 베이스의 문자집합을 ascii로 변경alter
# ALTER DATABASE test CHARACTER SET = ascii;
# SHOW VARIABLES LIKE 'character_set_database';

# 9) 데이터 베이스의 문자집합을 utf8로 변경
# ALTER DATABASE test CHARACTER SET = utfm64;
# SHOW VARIABLES LIKE 'character_set_database';

# 테이블 구조 변경(보통 컬럼에 대한 추가, 삭제, 변경)
# 10) 컬럼 추가(ADD)
# ALTER TABLE user2 ADD tmp TEXT;

# 11) 컬럼 변경 (MODIFY)
# ALTER TABLE user2 modify COLUMN tmp INT(3);

# 12) 컬럼 삭제 (DROP)
# ALTER TABLE user2 DROP tmp;

# 테이블 삭제
# DROP TABLE user2;

# 데이터 베이스 삭제
# DROP DATABASE test;



