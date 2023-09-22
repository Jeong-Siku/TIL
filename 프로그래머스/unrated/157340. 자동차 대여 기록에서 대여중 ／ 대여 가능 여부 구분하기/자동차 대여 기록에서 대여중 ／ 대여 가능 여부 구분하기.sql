-- 코드를 입력하세요
SELECT 
    CAR_ID,
    CASE
        WHEN date_format(START_DATE,"%Y-%m-%d")<="2022-10-16" and date_format(END_DATE,"%Y-%m-%d")>="2022-10-16" 
        THEN "대여중" 
        ELSE "대여 가능" 
    END as "AVAILABILITY"
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID desc;

SELECT 
    CAR_ID,
    CASE
        WHEN max("2022-10-16" between START_DATE and END_DATE)
        THEN "대여중" 
        ELSE "대여 가능" 
    END as "AVAILABILITY"
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
GROUP BY CAR_ID
ORDER BY CAR_ID desc;