def solution(n):
    for i in range(1,101):
        if 6*i%n==0:
            return i