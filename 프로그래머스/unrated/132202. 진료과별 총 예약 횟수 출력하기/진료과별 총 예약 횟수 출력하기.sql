-- 코드를 입력하세요
SELECT MCDP_CD "진료과 코드",
    count(MCDP_CD) 5월예약건수
from APPOINTMENT
where APNT_YMD like "2022-05%"
group by MCDP_CD
order by 5월예약건수 , MCDP_CD