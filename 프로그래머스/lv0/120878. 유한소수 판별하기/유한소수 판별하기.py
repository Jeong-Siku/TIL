def solution(a, b):
    answer = 0
    
    m약수 = 0
    for i in range(1,min(a,b)+1):
        if a%i==0 and b%i==0:
            m약수 = max(m약수,i)    
    
    a, b=a//m약수,b//m약수
    print(m약수)
    print(a,b)
    약수=[]
    for i in range(2,b+1):
        while b%i==0:
            b//=i
            약수.append(i)
    if all(i in (2,5) for i in 약수):
        return 1
    return 2