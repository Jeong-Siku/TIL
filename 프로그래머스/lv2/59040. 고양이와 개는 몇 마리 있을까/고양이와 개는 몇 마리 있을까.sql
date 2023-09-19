-- 코드를 입력하세요
SELECT ANIMAL_TYPE, count(ANIMAL_TYPE) as count
from ANIMAL_INS
where ANIMAL_TYPE = "Cat" or animal_type= "Dog"
group by ANIMAL_TYPE
order by ANIMAL_TYPE