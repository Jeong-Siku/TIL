USE test;

# 데이터 삽입 - INSERT 
INSERT INTO user1(user_id, name, email, age, rdate)
VALUES(1, 'mhso', 'minho_so@naver.com',36,'2023-05-25');

# 여러 개의 데이터를 동시에 삽입
INSERT INTO user1(user_id, name, email, age, rdate)
VALUES (2, 'park', 'mhso@gmail.com', 34, '2021-11-13'),
       (3, 'minho', 'mino@daum.net', 28, '2021-11-15'),
       (4, 'jiwon', 'jwon@daum.net', 27, '2021-11-11'),
       (5, 'siyeon', 'syw@snu.ac.kr', 25, '2021-11-12'),
       (6, 'taehee', 'thk@naver.com', 22, '2021-11-17');
       
# 특정 컬럼을 선택해서 데이터 삽입

INSERT INTO user1(user_id, name)
VALUES(7, 'sominho');

# 컬럼명을 지정하지 않으면 전체 컬럼에 INSERT
INSERT INTO user1
VALUES( 8, 'hahaha','asdf@naver.com',38,now());

select * from user1;

# 데이터 조회 SELECT
# SELECT 구문은 반드시 FROM 부터, SELECT는 제일 마지막에
SELECT name,email, rdate
FROM user1;

# *** 별명 붙이기(ALIAS)
SELECT user_id as "회원아이디",
		name as "회원이름",
        email as "회원이메일"

FROM user1

# 중복값 제거
# INSERT INTO user1 VALUES(9, 'haha', 'asdf@naver.com',38 , now());
SELECT * FROM user1;
SELECT DISTINCT(age) FROM user1;

# WHERE절(조건절) - Filtering
# 나이가 25세 이상인 사람들의 모든 정보 조회
SELECT * # 에스터리스크는 풀스캔을 하겠다는 의미이기에 웬만하면 안쓰는게 좋다. 오래 걸림
FROM user1
WHERE age >= 25;

# 2021년 11월 15일 이전에 가입한 사람의 이메일, 이름, 나이 조회
SELECT email,name,age
FROM user1
WHERE rdate < '2021-11-15';

# AND 연산
SELECT *
FROM user1
WHERE rdate >= '2021-11-12'
AND rdate <= '2021-11-15';

# BETWEEN 활용
SELECT *
FROM user1
WHERE rdate BETWEEN '2021-11-12' AND '2021-11-15';

# 나이가 30살 이상이고, 가입일이 2021-11-13일 이전인 사람의 모든 정보
SELECT *
FROM user1
WHERE age >= 30 
	AND rdate <= '2021-11-13';
    
# 나이가 20~35세, 가입일이 '2021-11-12 ~2021-11-15'인
# 사람들의 이름, 나이, 이메일, 가입일 조회
SELECT name,age,email,rdate
FROM user1
WHERE age BETWEEN 20 AND 35
	AND rdate BETWEEN '2021-11-12' AND '2021-11-15';
    
# GROUP BY
