# CEIL, ROUND, TRUNCATE

# 1) CEIL : 실수 데이터를 올림하여 정수로 나타내기
SELECT CEIL(12.345);

use world;
# 국가별 언어 사용 비율을 소수 첫번째 자리에서 올림하여 정수로 나타내기
SELECT CountryCode, Language, Percentage, CEIL(Percentage)
FROM countrylanguage;

# 2) ROUND : 실수 데이터를 반올림 할 때 사용한다.
SELECT ROUND(12.345, 2); # 소수점 셋째 자리에서 반올림하여 둘째 자리까지 표시

SELECT CountryCode, Language, Percentage, ROUND(Percentage,0)
FROM countrylanguage;

# 3) TRUNCATE : 실수 데이터를 버림 할 때 사용한다.
SELECT TRUNCATE(12.345,2); # 소수점 셋째 자리에서 내림하여 둘째 자리까지 표시

SELECT CountryCode, Language, Percentage, TRUNCATE(Percentage,0)
FROM countrylanguage;

# SQL에서 조건문을 사용할 수 있음. IF, CASE
# 1) IF(조건, 참 expr, 거짓 expr) # where은 필터링 느낌. IF조건은 where절 다음에 적용된다. 검사한다는 느낌.

# 도시의 인구가 100만이 넘으면 "Big City", 안넘으면 "Small City"
SELECT name, Population, IF(Population >= 1000000, "Big city", "Small City")
FROM city;

# 도시의 인구가 100만이 넘으면 "Big City", 50만이 넘으면 "Medium City", 안 넘으면 "Small City"
SELECT name,
	   Population,
       IF(
			Population >= 1000000,
            "Big City",
            IF(Population >= 500000,"Medium City","Small City")
		  )
FROM city; 

# NULL : 데이터가 없음을 의미
SELECT *
FROM country
WHERE IndepYear IS NULL;

SELECT *
FROM country
WHERE IndepYear IS NOT NULL;

# NULL값을 처리 -> NULL 대신에 다른 값으로 채우겠다.
# IFNULL(컬럼명, 채울 값)
SELECT IndepYear, IFNULL(IndepYear, 0),name
FROM country;

# CASE - END로 끝난다 , CASE를 쓸 때는 알리아스를 붙이는게 좋다.
-- CASE 
-- 	WHEN(조건1) THEN 출력1 ELSE,  # 필드에 대한 조건 (FILED : 한 칸에 대한 데이터)
--  WHEN(조건2) THEN 출력2 ELSE ,
-- END

# 나라 별로 인구가 10억 이상, 1억 이상, 1억 이하인 컬럼을 추가하여 표현
SELECT name,
	   population,
       CASE
			WHEN population >= 100000000 THEN '10억 이상'
            WHEN population >= 100000000 THEN '1억 이상'
			WHEN population < 100000000 THEN '1억 미만'
       END AS "result"
FROM country;

SELECT name
	   AVG(population) as avg_pop,
       CASE
			WHEN population >= 100000000 THEN '10억 이상'
            WHEN population >= 100000000 THEN '1억 이상'
			WHEN population < 100000000 THEN '1억 미만'
       END AS "result"
FROM country
GROUP BY result,name; # GROUP BY는 WHERE 다음에 실행. result에 포함되지않는 
				 # name을 select에 넣지않는다. 
                 # 목적으로 하지않는 기타 자료는 GROUP BY에 넣지 않는다.
                 # 기타 넣고 싶은 자료는 서브쿼리,조인 등을 사용하여 넣을 것
                 # 카테고리가 될 수 없는 컬럼은 절대 group by가 되어서는 안된다.
                 
# DATE_FORMAT(날짜 데이터(컬럼), 포매팅)
# 날짜 : 년-월-일 시:분:초
# 참고 : https://dev.mysql.com/doc/refman/5.7/en/date-and-time-functions.html
use sakila;

SELECT SUM(amount), DATE_FORMAT(payment_date, '%Y-%m') as "monthly"
FROM payment
GROUP BY monthly;

# 판다스로 작업하는 것은 처리가 완료된 데이터를 다룰 때. *반복문이 필요할 때. *복잡한 조건이 필요할 때. 
# Server의 성능이 좋기 떄문에. sql로 처리하는 것을 전제로 할 것.

# JOIN
# Table 간의 `관계성`을 이용해서 하나의 데이터로 합치는 것.
# PK-FK 이용
# PK : 대푯값(KEY). 유일한 값. 인덱스로 설정(일반적으로 정수로 설정). 색인(index). 정렬.
# UK : 유일성. 단, 참조 불가능(FK가 될 수 없다.)
# FK : 외래키. 중복 가능. PK를 참조. 참조무결성제약 조건 , Constraint 중요.

# 집합레벨 : FROM절에 존재하는 테이블은 집합레벨 1인 것이 이상적. 관계성을 만들기 좋다.

# JOIN
CREATE DATABASE test;
USE test;
CREATE TABLE user (
	user_id int(11) unsigned NOT NULL AUTO_INCREMENT, name varchar(30) DEFAULT NULL,
	PRIMARY KEY (user_id)
);

CREATE TABLE addr (
	id int(11) unsigned NOT NULL AUTO_INCREMENT, addr varchar(30) DEFAULT NULL,
	user_id int(11) DEFAULT NULL,
	PRIMARY KEY (id)
);

INSERT INTO user(name) VALUES ("jin"),
("po"),
("alice"),
("petter");
INSERT INTO addr(addr, user_id) VALUES ("seoul", 1),
("pusan", 2),
("deajeon", 3),
("deagu", 5), ("seoul", 6);

# INNER JOIN : 두 테이블 사이에 공통된 값이 없는 row는 출력 안함.
SELECT user.user_id, user.name, addr.addr # 알리아스로 대체 가능
FROM user # main으로 생각하는 테이블을 놓는다. 관심있는
JOIN addr ON user.user_id = addr.user_id;# user에 addr을 추가. 공통점을 바탕으로

use world;
# 도시이름과 국가이름을 출력
# 도시 : city, 국가이름 : country 테이블
desc city;
desc country;

select * from city;
select * from country;

SELECT city.name as "city_name", country.name as "country_name"
FROM city
JOIN country ON city.CountryCode = country.Code;

# LEFT JOIN
# FROM절에 오는 테이블의 모든 정보를 표시.
use test;

SELECT user.user_id, user.name, addr.addr
FROM user
LEFT JOIN addr ON user.user_id = addr.user_id;

# RIGHT JOIN
SELECT addr.user_id, user.name, addr.addr
FROM user
RIGHT JOIN addr ON user.user_id = addr.user_id;

# UNION
# SELECT 문의 결과 데이터를 하나로 합쳐서 출력.
# 주의해야할 것 : 컬럼의 개수와, 타입, 순서가 모두 일치해야 한다.
# UNION은 자동으로 distinct가 적용된다. (중복 데이터는 제거됨)
# UNION ALL은 중복을 허용
SELECT name FROM user
UNION
SELECT addr FROM addr;

SELECT name FROM user
UNION ALL
SELECT addr FROM addr;

# UNION으로 FULL Outer JOIN 구현
SELECT user.user_id, user.name, addr.addr
FROM user
LEFT JOIN addr ON user.user_id = addr.user_id

UNION

SELECT user.user_id, user.name, addr.addr
FROM user
RIGHT JOIN addr ON user.user_id = addr.user_id;

-- 1. countrylanguage 테이블에서 countrycode가 'NA'로 시작하는 국가의 언어들중, 사용자의 언어percentage가 10이상 30이하인 언어를 percentage순으로 오름차순 정렬
use world;

SELECT CountryCode, Percentage
FROM countrylanguage
WHERE CountryCode like "NA%" 
	  AND Percentage BETWEEN 10 AND 30
ORDER BY Percentage ASC;

-- 2. countrylanguage 테이블에서 contrycode별 공식적인 언어(isofficial이 T)와 평균 퍼센테이지를 조회하고 평균 퍼센테이지를 내림차순으로 정렬
SELECT CountryCode, isofficial, AVG(Percentage)
FROM countrylanguage
WHERE IsOfficial='T' 
GROUP BY CountryCode
ORDER BY AVG(Percentage) DESC;

-- 3. city 테이블의 국가코드별 도시의 개수를 구하세요. 단 도시가 50개 이상인 국가만 표시하세요.
SELECT CountryCode, COUNT(CountryCode) as count_city
FROM city
GROUP BY CountryCode
HAVING count_city>= 50;

-- 4. country 테이블에서 독립년도가 1901~1999인 지역 중에서, 정부형태(GovenrnmentForm)가 Republic이면서 평균 GNP가 6000 이상인 지역
SELECT LocalName, indepYear,GovernmentForm, GNP
FROM country
WHERE indepYear BETWEEN 1901 AND 1999 
	  AND (GovernmentForm = "Republic" AND GNP>=6000);

-- 5.country 테이블에서 Region별   surfaceArea, Capital 평균 및 GNP합계 구하시오 (단 Capital은 30 이상인곳만 조회,하고 오름차순 정렬) 
SELECT Region, AVG(surfaceArea), AVG(Capital), SUM(GNP)
FROM country
WHERE Capital >= 30
GROUP BY Region
ORDER BY AVG(Capital) ASC;

-- city 테이블에서, CountryCode가 A로 시작하면서 인구가 50만명 이상인 국가의 이름, CountryCode, Population을 구하고, 인구 수를 기준으로 내림차순 정리
SELECT Name, CountryCode, Population
FROM city
WHERE CountryCode like "A%" 
	AND Population >=500000
ORDER BY Population DESC;

-- country 테이블에서 대륙별 국가이름, 지역, 평균 독립년도와 평균 예상 수명을 조회하고 남아메리카와 아프리카 대륙을 제외, 독립년도가 20세기 이후인 국가들 중 공화국(republic)인 나라들의 데이터를 구하시오. 평균 독립년도는 오름차순, 평균 예상 수명은 내림차순으로 정렬.
SELECT AVG(indepYear), AVG(LifeExpectancy)
FROM country
WHERE Continent NOT IN ('North America','Africa')
		AND IndepYear>=1900 
        AND GovernmentForm = 'republic'
GROUP BY Continent
ORDER BY AVG(indepYear) ASC, AVG(LifeExpectancy) DESC;

SELECT Continent
FROM country;

-- 대륙, 국가, 인구수, GNP, 예상 수명의 상관 관계를 조사하기 위해 country 테이블에서 대륙, 대륙별 평균 GNP, 대륙별 예상 평균 수명, 국가, 인구수, GNP, 예상 수명을 조회하고 각각의 컬럼 값이 Null인 국가는 조회하지 않으며, 인구 수가 10000명 이하의 국가는 제외하여 구한다. 평균 수명과 평균 GNP는 내림차순으로 정렬한다.
SELECT Continent, AVG(GNP), AVG(LifeExpectancy),Name, Population, GNP, LifeExpectancy
FROM country 
WHERE Population >=10000
Group By Continent
HAVING Population IS NOT NULL 
ORDER BY AVG(GNP) DESC,AVG(LifeExpectancy) DESC;