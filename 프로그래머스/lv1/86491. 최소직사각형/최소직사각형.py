def solution(sizes):
    # max,min 배열로 맞추기
    answer = 0
    l_max = 0
    r_max = 0
    for l,r in sizes:
        if l<r:
            l,r = r,l
        l_max=max(l_max,l)
        r_max=max(r_max,r)
        
    return l_max*r_max