-- 코드를 입력하세요
SELECT truncate(PRICE,-4) as PRICE_GROUP, count(PRICE) as PRODUCTS
from PRODUCT
group by PRICE_GROUP
order by PRICE_GROUP