-- 코드를 입력하세요
SELECT h.flavor
FROm FIRST_HALF h
join ICECREAM_INFO i on h.FLAVOR = i.flavor
WHERE TOTAL_ORDER >= 3000 
    and INGREDIENT_TYPE = "fruit_based"