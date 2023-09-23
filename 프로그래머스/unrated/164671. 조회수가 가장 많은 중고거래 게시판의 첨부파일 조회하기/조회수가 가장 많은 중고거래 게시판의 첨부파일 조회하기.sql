-- 코드를 입력하세요
SELECT concat("/home/grep/src/",B.BOARD_ID,"/",FILE_ID,FILE_NAME,FILE_EXT) FILE_PATH
# 자동으로 브로드캐스팅처럼 확장된다.
FROM USED_GOODS_BOARD B, USED_GOODS_FILE F
WHERE B.BOARD_ID = F.BOARD_ID
    AND B.VIEWS = (select max(USED_GOODS_BOARD.views) from USED_GOODS_BOARD)
ORDER BY FILE_ID desc;
    # limit는 동일한 id에 해당하는 여러개의 첨부파일 경로를 보여주지 못한다.