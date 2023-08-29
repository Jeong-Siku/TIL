def solution(n):
    answer = [0]
    idx=0
    cur=0
    while idx<101:
        nex=cur+1
        if not nex%3 or "3" in str(nex):
            cur+=1
        else:
            idx+=1
            cur = nex
            answer.append(cur) 
    return answer[n]