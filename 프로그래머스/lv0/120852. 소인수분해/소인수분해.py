def solution(n):
    소인수 = []
    for i in range(2,n+1):
        cnt = 0
        for j in range(2,i+1):
            if i%j==0:
                cnt+=1
        if cnt==1:
            소인수.append(i)
            
    result = []
    for i in 소인수:
        if n%i==0:
            result.append(i)
    
    return result

def solution(n):
    answer = []
    d = 2
    while n!=1:
        if n%d==0:
            if d not in answer:
                answer.append(d)
            n/=d
        else:
            d+=1
    return answer