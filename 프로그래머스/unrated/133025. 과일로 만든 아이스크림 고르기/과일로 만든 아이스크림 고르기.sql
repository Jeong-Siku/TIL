-- 코드를 입력하세요
SELECT h.flavor
FROm FIRST_HALF h
join ICECREAM_INFO i on h.FLAVOR = i.flavor
WHERE TOTAL_ORDER >= 3000 
    and INGREDIENT_TYPE = "fruit_based";
    
select flavor
from FIRST_HALF
where flavor 
    in (select flavor
       from ICECREAM_INFO
       where INGREDIENT_TYPE = "fruit_based")
       and TOTAL_ORDER >= 3000
order by TOTAL_ORDER DESC