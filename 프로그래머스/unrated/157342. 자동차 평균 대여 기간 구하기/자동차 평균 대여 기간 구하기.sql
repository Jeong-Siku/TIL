-- 코드를 입력하세요

# date 자료는 datediff(end_date,start_date) 메소드 사용
SELECT CAR_ID,round(avg(datediff(END_DATE,START_DATE)+1),1) AVERAGE_DURATION
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by CAR_ID
having avg(datediff(END_DATE,START_DATE)+1)>=7
order by AVERAGE_DURATION desc,CAR_ID desc;
