def solution(t, p):
    answer = 0
    # 범위
    # 문자열
    # 비교
    for i in range(len(t)-len(p)+1):
        if t[i:i+len(p)] <= p:
            answer+=1
    return answer