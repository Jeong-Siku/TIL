-- 코드를 입력하세요
SELECT ANIMAL_ID
FROM animal_ins
Where NAME is not null
    and DATETIME is not null
order by ANIMAL_ID asc