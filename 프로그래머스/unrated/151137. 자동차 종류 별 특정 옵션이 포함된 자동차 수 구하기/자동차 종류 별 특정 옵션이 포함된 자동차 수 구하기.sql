-- 코드를 입력하세요
SELECT CAR_TYPE,count(*) as CARS
from CAR_RENTAL_COMPANY_CAR
where OPTIONS like "%통풍시트%" or 
    OPTIONS like "%열선시트%" or 
    OPTIONS like "%가죽시트%"
group by CAR_TYPE
order by CAR_TYPE asc;

SELECT car_type, COUNT(*) CARS
FROM CAR_RENTAL_COMPANY_CAR
WHERE options REGEXP '통풍시트|열선시트|가죽시트'
GROUP BY car_type
ORDER BY car_type;