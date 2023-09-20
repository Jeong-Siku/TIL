-- 코드를 입력하세요
SELECT HOUR(DATETIME) HOUR, count(DATETIME) COUNT
from ANIMAL_OUTS
where HOUR(DATETIME) between 9 and 19
group by HOUR
order by HOUR