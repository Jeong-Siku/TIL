def solution(n):
    answer = 0
    for i in range(1,n+1):
        if n%i==0:
            answer+=1
    return answer

def solution(n):
    return len(list(filter(lambda x : n%(x+1)==0,range(n))))