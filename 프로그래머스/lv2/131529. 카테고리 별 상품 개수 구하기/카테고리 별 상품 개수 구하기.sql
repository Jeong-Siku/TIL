-- 코드를 입력하세요
SELECT left(PRODUCT_CODE,2) CATEGORY, count(left(PRODUCT_CODE,2)) PRODUCTS
FROM PRODUCT
GROUP BY left(PRODUCT_CODE,2)
ORDER BY CATEGORY