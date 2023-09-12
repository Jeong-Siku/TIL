def solution(n, m):
    answer = []
    n_div = []
    m_div = []
    for i in range(1,int(n**0.5)+1):
        if not n%i:
            n_div.append(i)
            if i**2 != n:
                n_div.append(n//i)
    
    for i in range(1,int(m**0.5)+1):
        if not m%i:
            m_div.append(i)
            if i**2 != m:
                m_div.append(m//i)
    max_div = 0
    for i in sorted(n_div):
        if i in m_div:
            max_div = max(i,max_div)
            
    
    return max_div,(n//max_div)*(m//max_div)*max_div

# 유클리드 호제법
def solution(n, m):
    c,d=max(n,m) , min(n,m)
    t=1
    while t!=0:
        t=c%d
        c,d = d,t
        # 두개의 값을 나눈 나머지를 계속 반복하여 나머지가 0이면 마지막 나눈 값이 최대공배수
        # 최소공배수는 두개의 값을 곱한뒤 최대공약수로 나눈 값
    return c, n*m//c