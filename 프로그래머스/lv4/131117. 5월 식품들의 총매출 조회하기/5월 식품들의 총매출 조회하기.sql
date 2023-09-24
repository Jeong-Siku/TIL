-- 코드를 입력하세요
SELECT P.PRODUCT_ID, PRODUCT_NAME, sum(PRICE*AMOUNT) TOTAL_SALES
FROM FOOD_PRODUCT P, FOOD_ORDER O
WHERE P.PRODUCT_ID = O.PRODUCT_ID
    AND date_format(PRODUCE_DATE,"%Y-%m") = "2022-05"
GROUP BY P.PRODUCT_ID
ORDER BY TOTAL_SALES desc, P.PRODUCT_ID