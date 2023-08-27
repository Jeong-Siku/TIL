def solution(n):
    for i in range(1,1001):
        if i*i == n:
            return 1
    return 2