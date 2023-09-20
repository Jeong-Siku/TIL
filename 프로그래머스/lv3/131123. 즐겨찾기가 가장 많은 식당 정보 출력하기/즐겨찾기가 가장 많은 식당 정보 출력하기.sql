-- 코드를 입력하세요 
select FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
from (
    SELECT *,
        sum(FAVORITES) as best,
        rank() over(partition by FOOD_TYPE order by sum(FAVORITES) desc) as ranking
    from REST_INFO
    group by REST_NAME,FOOD_TYPE
    order by FOOD_TYPE desc,best desc) C
where ranking = 1
