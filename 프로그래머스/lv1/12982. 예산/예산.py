def solution(d, budget):
    d.sort()
    d_sum = 0
    result = 0
    for i in d:
        d_sum+=i
        if d_sum<=budget:
            result+=1
    return result