-- 코드를 입력하세요
SELECT USER_ID,NICKNAME, sum(price) TOTAL_SALES
from 
    (select *
    from USED_GOODS_BOARD b, USED_GOODS_USER u
    where b.WRITER_ID = u.USER_ID
        and b.STATUS = "DONE") c
group by WRITER_ID
having sum(price) >= 700000
order by TOTAL_SALES asc;
