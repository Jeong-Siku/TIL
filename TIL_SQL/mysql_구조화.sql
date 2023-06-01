create database sql_analyze;
use sql_analyze;

DROP TABLE TB_TEMPER_DATA;
DROP TABLE TB_TEMPER;

CREATE TABLE TB_TEMPER_DATA
(
  STD_DE VARCHAR(10)
, AREA_CD VARCHAR(3)
, AVG_TEMPER DECIMAL(3, 1)
, MIN_TEMPER DECIMAL(3, 1)
, MAX_TEMPER DECIMAL(3, 1)
);

SELECT * FROM TB_TEMPER_DATA;
# 자료는 만들어진 테이블에 오른쪽 클릭하여 Table Data import Wizard를 사용하여 넣는다

SELECT COUNT(*) FROM TB_TEMPER_DATA WHERE AREA_CD IS NULL;
-- DELETE FROM TB_TEMPER_DATA WHERE AREA_CD IS NULL;

CREATE TABLE TB_TEMPER
(
  STD_DE VARCHAR(8)
, AREA_CD VARCHAR(3)
, AVG_TEMPER DECIMAL(3, 1)
, MIN_TEMPER DECIMAL(3, 1)
, MAX_TEMPER DECIMAL(3, 1)
, PRIMARY KEY (STD_DE, AREA_CD)
);

# 참고자료 : https://data.kma.go.kr/cmmn/main.do

SET SQL_SAFE_UPDATES = 0;
# 사용자가 실수로 여러 데이터를 삭제하는 일을 방지하는 모드인 Safe mode가 디폴트로 설정되어있음
# SELECT 조건절에 PK가 아닌 키를 사용할 수 없음.
# 0은 safe update mode를 해제
DELETE FROM TB_TEMPER_DATA WHERE AREA_CD IS NULL;
# 데이터가 두 번 들어가면 duplicator 에러가 뜬다. 테이블을 모두 드랍한 뒤 파이썬에서 다시 데이터를 넣는다. 

INSERT INTO TB_TEMPER
SELECT
   REPLACE(STD_DE, '-', '') AS STD_DE
 , AREA_CD
 , AVG_TEMPER
 , MIN_TEMPER
 , MAX_TEMPER
  FROM TB_TEMPER_DATA;

COMMIT;

select * from TB_TEMPER;

-- 날짜 , 서울 코드, 평균기온, 최저기온, 최고기온
# 서울시의 최고 / 최저 온도 및 해당 일자 구하기
	# 집계와 조회의 대상을 각각 구분할 것! 집계와 조회는 동시에 불가능!

	# step 1) 서울시의 역사상 최저 및 최고 온도를 구한다.
SELECT 
	TEMPER_MIN_MAX_SEOUL.AREA_CD,
    MIN(TEMPER_MIN_MAX_SEOUL.MIN_TEMPER) AS MIN_TEMPER,
    MAX(TEMPER_MIN_MAX_SEOUL.MAX_TEMPER) AS MAX_TEMPER
    
FROM TB_TEMPER AS TEMPER_MIN_MAX_SEOUL
WHERE TEMPER_MIN_MAX_SEOUL.AREA_CD = '108'
GROUP BY TEMPER_MIN_MAX_SEOUL.AREA_CD;
	
    # step 2) 일자 찾기
SELECT B.AREA_CD,
	   B.STD_DE,
       B.MIN_TEMPER,
       B.MAX_TEMPER
FROM (
	SELECT 
		TEMPER_MIN_MAX_SEOUL.AREA_CD,
		MIN(TEMPER_MIN_MAX_SEOUL.MIN_TEMPER) AS MIN_TEMPER,
		MAX(TEMPER_MIN_MAX_SEOUL.MAX_TEMPER) AS MAX_TEMPER
    
	FROM TB_TEMPER AS TEMPER_MIN_MAX_SEOUL
	WHERE TEMPER_MIN_MAX_SEOUL.AREA_CD = '108'
	GROUP BY TEMPER_MIN_MAX_SEOUL.AREA_CD) as MINMAX_TEMPER
JOIN TB_TEMPER B on (B.AREA_CD = MINMAX_TEMPER.AREA_CD AND 
					 B.MIN_TEMPER = MINMAX_TEMPER.MIN_TEMPER) OR# self-join 
                     (B.AREA_CD = MINMAX_TEMPER.AREA_CD AND
                     B.MAX_TEMPER = MINMAX_TEMPER.MAX_TEMPER);

 # 과제 : 본인 생일 (월-일) 기준으로 역사상 서울시의 최고 기온과 최저 기온 및 이에 해당하는 날짜
 
 # 1년 중 평균 일교차가 가장 큰 달을 구하기
 SELECT date_format(std_de, '%m') as MM,
		avg(MAX_temper - min_temper) as DAILY_CROSS
 FROM TB_TEMPER
 WHERE area_cd = '108'
 GROUP BY MM
 ORDER BY DAILY_CROSS DESC
 LIMIT 1;
 
 # 역사상 서울시를 기준으로 일교차가 가장 큰 날, 해당 일의 일교차, 최저온도, 최고 온도 구하기
 
	#subquery_from절 
 select std_de,
		(max_temper - min_temper),
        min_temper,
        max_temper
 from TB_TEMPER
 where area_cd = '108'
 order by (max_temper - min_temper) desc;
	# 결과
 select 
	std_de,
	(max_temper - min_temper),
	min_temper,
	max_temper
 from (
	 select std_de,
		(max_temper - min_temper) as daily_cross,
        min_temper,
        max_temper
	 from TB_TEMPER
	 where area_cd = '108' -- 지역코드 : 서울특별시 
						   # 추후에 다른 테이블과 엮일 여지가 있다면 서브쿼리를 짜는 것이 편의성을 높일 수 있다.
	 order by daily_cross desc) as SEOUL_TEMPER
limit 1;
 
 # 연도 별 평균 기온 변화 확인하기
 select 
		date_format(std_de,'%Y'),
		round(avg(avg_temper),2)
 from TB_TEMPER
 where TB_TEMPER.AREA_CD = '108'
 group by date_format(std_de,'%Y');
 
 # 연대 별 평균 기온을 구하기
# 1900-1909 : 1900년대
# 1910-1919 : 1910년대

#서브쿼리로 활용
SELECT 
		CASE
			WHEN YYYY BETWEEN '1900' AND '1909' THEN '1900년대' WHEN YYYY BETWEEN '1910' AND '1919' THEN '1910년대'
			WHEN YYYY BETWEEN '1920' AND '1929' THEN '1920년대' WHEN YYYY BETWEEN '1930' AND '1939' THEN '1930년대'
			WHEN YYYY BETWEEN '1940' AND '1949' THEN '1940년대' WHEN YYYY BETWEEN '1950' AND '1959' THEN '1950년대'
			WHEN YYYY BETWEEN '1960' AND '1969' THEN '1960년대' WHEN YYYY BETWEEN '1970' AND '1979' THEN '1970년대'
			WHEN YYYY BETWEEN '1980' AND '1989' THEN '1980년대' WHEN YYYY BETWEEN '1990' AND '1999' THEN '1990년대'
			WHEN YYYY BETWEEN '2000' AND '2009' THEN '2000년대' WHEN YYYY BETWEEN '2010' AND '2019' THEN '2010년대'
			WHEN YYYY BETWEEN '2020' AND '2029' THEN '2020년대' 
		END as "연대",
        AVG(A.AVG_TEMPER) as "평균기온"
FROM (
		SELECT DATE_FORMAT(A.STD_DE, '%Y') AS YYYY
			 , ROUND(AVG(AVG_TEMPER), 2) AS AVG_TEMPER
		  FROM TB_TEMPER A
		 WHERE A.AREA_CD = '108' -- 지역코드 : 서울특별시
		 GROUP BY YYYY
		 ORDER BY YYYY ) as A
-- GROUP BY "연대"; # CASE문은 다이나믹하기 때문에 카테고리로 구분 불가능 . 들어가는 데이터에 따라 값이 달라진다.
GROUP BY CASE # GROUP BY CASE문을 통해 카테고리 구분 가능. 이미 완성된 내용을 바탕으로
			WHEN YYYY BETWEEN '1900' AND '1909' THEN '1900년대' WHEN YYYY BETWEEN '1910' AND '1919' THEN '1910년대'
			WHEN YYYY BETWEEN '1920' AND '1929' THEN '1920년대' WHEN YYYY BETWEEN '1930' AND '1939' THEN '1930년대'
			WHEN YYYY BETWEEN '1940' AND '1949' THEN '1940년대' WHEN YYYY BETWEEN '1950' AND '1959' THEN '1950년대'
			WHEN YYYY BETWEEN '1960' AND '1969' THEN '1960년대' WHEN YYYY BETWEEN '1970' AND '1979' THEN '1970년대'
			WHEN YYYY BETWEEN '1980' AND '1989' THEN '1980년대' WHEN YYYY BETWEEN '1990' AND '1999' THEN '1990년대'
			WHEN YYYY BETWEEN '2000' AND '2009' THEN '2000년대' WHEN YYYY BETWEEN '2010' AND '2019' THEN '2010년대'
			WHEN YYYY BETWEEN '2020' AND '2029' THEN '2020년대' 
		END
ORDER BY "연대";        