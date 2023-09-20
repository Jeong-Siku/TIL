-- 코드를 입력하세요 
select FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
from (
    SELECT *,
        sum(FAVORITES) as best,
    # over의 순서는 partition by 다음 order by
    # over()에서 ,는 쓰지 않는다.
        rank() over(partition by FOOD_TYPE order by sum(FAVORITES) desc) as ranking
    from REST_INFO
    group by REST_NAME,FOOD_TYPE
    order by FOOD_TYPE desc,best desc) C
where ranking = 1;

# rank를 사용하면 굳이 groupby를 사용하지않아도 된다.
# 가장 큰수를 구할때는 max를 사용해도 됨
select FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
from (
    SELECT *,
        rank() over(partition by FOOD_TYPE order by FAVORITES desc) as ranking
    from REST_INFO
    ) C
where ranking = 1
order by FOOD_TYPE desc;
