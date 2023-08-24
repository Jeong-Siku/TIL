-- 코드를 입력하세요
SELECT BOOK_ID, date_format(PUBLISHED_DATE,"%Y-%m-%d")
FROM BOOK
WHERE date_format(PUBLISHED_DATE,"%Y") = 2021 and
    CATEGORY="인문"