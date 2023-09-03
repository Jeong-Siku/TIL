def solution(k, m, score):
    # 최대값
    # 최소인 값을 최대로 
    answer = 0
    score.sort(reverse=True)
    for i in range(0,len(score),m):
        if len(score[i:i+m])==m:
            answer+=len(score[i:i+m])*min(score[i:i+m])
        
    return answer