-- 코드를 입력하세요
SELECT CATEGORY,sum(SALES) as TOTAL_SALES
from BOOK_SALES as sale
join book as b on sale.book_id = b.book_id
where SALES_DATE like "2022-01%"
group by CATEGORY
order by CATEGORY