-- 코드를 입력하세요
with a as (
    # 이렇게 할 시 그룹별로 하나의 값만 나온다.
    select CAR_ID
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY
    where START_DATE between "2022-08-01" and "2022-10-31"
    group by CAR_ID
    having count(*)>=5
    )
    
SELECT month(start_date) MONTH, a.CAR_ID, count(*) RECORDS
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY h, a
where a.CAR_ID = h.CAR_ID
    and start_date between "2022-08-01" and "2022-10-31"
group by month,a.CAR_ID
order by MONTH asc, a.CAR_ID desc;