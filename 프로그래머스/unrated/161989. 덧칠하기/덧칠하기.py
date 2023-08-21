def solution(n, m, section):
    paint = [0 for _ in range(n)] 
    
    
    for i in section:
        paint[i-1]=1
    
    cnt = 0
    for i in range(len(section)):
        if paint[section[i]-1]==1:
            for j in range(section[i]-1,section[i]-1+m):
                if j<= n-1:
                    paint[j] = 0
            cnt+=1

    return cnt

def solution(n, m, section):
    answer = 1
    
    prev = section[0]
    for sec in section:
        if sec-prev<m:
            pass
        elif sec-prev >=m:
            answer+=1
            prev= sec
    return answer 