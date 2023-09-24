-- 코드를 입력하세요
SELECT U.USER_ID, 
    NICKNAME, 
    concat(CITY," ",STREET_ADDRESS1," ",STREET_ADDRESS2) 전체주소, 
    concat(substring(TLNO,1,3),"-",substring(TLNO,4,4),"-",substring(TLNO,8,4)) 전화번호
FROM USED_GOODS_BOARD B, USED_GOODS_USER U
WHERE B.WRITER_ID = U.USER_ID
GROUP BY B.WRITER_ID
HAVING count(B.WRITER_ID) >= 3 
ORDER BY U.USER_ID desc;