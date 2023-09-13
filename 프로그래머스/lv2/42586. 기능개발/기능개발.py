def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i]=progresses[i]+speeds[i]

        cnt=0
        # progresses가 있는지 확인안하면 인덱스 에러가 뜬다.
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1
        if cnt>0:
            answer.append(cnt)
    
    return answer