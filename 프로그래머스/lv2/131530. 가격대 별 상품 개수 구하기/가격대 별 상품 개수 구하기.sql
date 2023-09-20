-- 코드를 입력하세요

# 오라클
SELECT truncate(PRICE,-4) as PRICE_GROUP, count(PRICE) as PRODUCTS
from PRODUCT
group by PRICE_GROUP
order by PRICE_GROUP

# # mysql
# SELECT (PRICE-PRICE%10000) as PRICE_GROUP, count(PRICE) as PRODUCTS
# from PRODUCT
# group by PRICE_GROUP
# order by PRICE_GROUP