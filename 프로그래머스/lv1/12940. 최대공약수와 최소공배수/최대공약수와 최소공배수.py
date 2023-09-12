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