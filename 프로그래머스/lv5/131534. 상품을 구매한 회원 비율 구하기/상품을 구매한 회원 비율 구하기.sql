-- 코드를 입력하세요
# with a as (select count(*) from USER_INFO where year(JOINED)="2021")

SELECT YEAR(SALES_DATE) YEAR,
        MONTH(SALES_DATE) MONTH,
        count(distinct(user_id)) PUCHASED_USERS,
        round(count(distinct(user_id))/(select count(*) from USER_INFO where year(JOINED)="2021"),1) PUCHASED_RATIO
FROM ONLINE_SALE
WHERE USER_ID in 
                (select USER_ID FROM USER_INFO
                where year(JOINED) = "2021")
GROUP BY YEAR,month
ORDER BY YEAR,month;
