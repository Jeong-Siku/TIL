# GROUP By는 특정 컬럼을 기준으로 데이터를 묶은 다음
# 각종 집계 함수를 이용해 데이터를 집계(Aggregate)
# SUM, AVG, STD, STDDEV, VAR, MAX, MIN, COUNT 등등..
use world;

SELECT *
FROm city;

# 국가 코드 별 몇개의 도시가 있는지?
SELECT CountryCode, COUNT(CountryCode)
FROM city
GROUP BY CountryCode;

# select distinct(countrycode) from world

# 각 국가마다 인구의 평균 구하기(AVG)
SELECT AVG(population)
FROM city
GROUP BY CountryCode;

# 1) 인구수가 23만명 이하 이거나 50만명 이상인 나라들의 국가 별 인구수 평균
SELECT CountryCode, AVG(population)
FROM city
WHERE Population <= 230000 or Population >= 500000 # 조건으로 먼저 필터링 된 뒤에 그룹핑한다.
GROUP BY CountryCode;

# 2) 국가 코드가 A로 시작하는 나라(like 'A%') 중 인구수가
# 23만명 이하이거나 50만명 이상인 나라들의 국가 별 인구수 평균

# 연산자의 우선순위
# OR AND 가 있으면 AND가 우선순위를 가진다.
SELECT CountryCode, AVG(population)
FROM city
WHERE (Population <= 230000 or Population >= 500000) AND # 1) 인구수가 23만명 이하 이거나 50만명 이상인 나라들의 국가 별 인구수 평균
SELECT CountryCode, AVG(population)
FROM city
WHERE Population <= 230000 or Population >= 500000
GROUP BY CountryCode;

# 2) 국가 코드가 A로 시작하는 나라(like 'A%') 중 인구수가
# 23만명 이하이거나 50만명 이상인 나라들의 국가 별 인구수 평균
SELECT CountryCode, AVG(population)
FROM city
WHERE CountryCode like 'A%' and (Population <= 230000 or Population >= 500000)
GROUP BY CountryCode;

# CountryCode, district 별 인구수 평균
# 부분집합을 만드는 것과 흡사
SELECT countrycode , district,AVG(population)
FROM city
GROUP BY CountryCode , district;

# 각 district 별 인구수 평균, 표준편차, 최댓값, 최솟값, 
# district 조회 후 표준편차 내림차순 정렬
# ORDER BY는 SELECT보다 후순위
SELECT district, 
	AVG(population), 
    STDDEV(population) as pop_std, 
    MAX(population),
    MIN(population)
FROM city
GROUP BY district
ORDER BY pop_std DESC;
# ORDER BY 3 DESC; # SELECT 뒤이기 때문에 알리아스가 이뤄진 뒤에 기능한다.

# HAVING 절
# GROUP BY에 대한 조건절
# WHERE은 FROM에 대한 조건절(테이블에 대한 필터)
# HAVING은 집계 결과에 대한 조건절 (SELECT에 대한 필터링)

# 인구수의 총 합이 5천만 이상인 나라만 조회
SELECT CountryCode, 
	   SUM(Population) as "sum_pop"
FROM city
GROUP BY CountryCode
HAVING sum_pop >= 50000000;

# LIMIT - 표시되는 테이블의 로우 개수 제한
select *
from city 
limit 1, 3;