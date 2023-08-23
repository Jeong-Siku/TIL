def solution(n):
    answer = 1
    for i in range(1,n+1):
        answer*=i
        if answer*(i+1)>n:
            return i