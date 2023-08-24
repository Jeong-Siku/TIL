-- 코드를 입력하세요
SELECT info.REST_ID, info.REST_NAME, info.FOOD_TYPE, info.FAVORITES,info.ADDRESS, round(avg(review.REVIEW_SCORE),2) as SCORE
FROM REST_INFO as info
JOIN REST_REVIEW as review on info.REST_ID = review.REST_ID
WHERE info.ADDRESS like "서울%"
GROUP BY info.REST_NAME
ORDER BY SCORE DESC,FAVORITES DESC
