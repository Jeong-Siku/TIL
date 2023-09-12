def solution(n):
    answer = 0
    for i in range(2,n+1):
        for j in range(2,int(i**0.5)+1):
            if not i%j:
                break
        else:
            answer+=1
    return answer

# 에라토스테네스의 체
def solution(n):
    list_n = [True for _ in range(n+1)]
    answer = 0
    for i in range(2,int(n**0.5)+1):
        if list_n[i] ==True:
            j=2
            while i*j<=n:
                list_n[i*j]=False
                j+=1
    for j in range(2,n+1):
        if list_n[j]:
            answer+=1
    return answer
                