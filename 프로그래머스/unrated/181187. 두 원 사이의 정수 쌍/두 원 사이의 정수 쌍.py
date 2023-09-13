from math import ceil, floor, sqrt
def solution(r1, r2):
    answer = 0
    for i in range(1,r2+1):
        max_y = floor(sqrt(r2**2-i**2))
        min_y = ceil(sqrt(r1**2-i**2)) if i<r1 else 0
        answer+=max_y-min_y+1
    return answer*4
