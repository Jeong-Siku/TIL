use world;

# select절에서 서브쿼리 사용하기. 하나의 값으로 구성할 것

	# 전체 나라 수, 전체 도시 수, 전체 언어의 수를 출력
select
	(select count(*) from city) as toal_city,
    (select count(*) from country) as total_country,
    (select count(*) from countrylanguage)as total_language
from dual; # 듀얼테이블 = 더미테이블, 이 부분은 생략 가능.

# 800만 이상되는 도시의 국가코드, 이름, 도시인구수 출력
# step 1) city 테이블 필터링 하기
select * from city;
# 아래에 필터링 된 테이블을 사용한다. FROM절에 테이블 역할을 할 수 있다.
# FROM절인 것 마냥 사용 가능. 따로 형태에 제약 없음
SELECT name as "city_name", countrycode, population
FROM city # city를 미리 줄여둔 상태에서 원하는 값을 뽑는 것이 퍼포먼스에서 더 좋다. 
		  # From 절의 역할 -> Table 불러오기
WHERE population >= 8000000;

	# step 2) 서브 쿼리로 사용하기(from 절)
	# 서브쿼리로 FROM절에 테이블을 사용하면 알리아스를 꼭 지어줄 것
select *

from ( SELECT name as "city_name", 
				countrycode, 
                population
		FROM city 
		WHERE population >= 8000000) as city_pop_over_800; # 알리아스 필수 !
        
	# step 3) 다른 테이블과의 JOIN. 같은 테이블과의 조인을 수행하는 것을 self-join이라고 한다.
select city_pop_over_800.city_name,
	   country_simple.name,
       city_pop_over_800.population

from ( SELECT name as "city_name", 
				countrycode, 
                population
		FROM city 
		WHERE population >= 8000000) as city_pop_over_800
        
join (select code, name from country) as country_simple 
  on city_pop_over_800.countrycode = country_simple.code;
  
# WHERE 절 subquery. 컬럼형태

	# 800만 이상 도시의 국가코드, 국가이름, 대통령 이름
select code, name

from country

where code in (select distinct(countrycode)
			   from city 
			   where population >= 8000000) ; # 판다스의 시리즈 역할을 한다.