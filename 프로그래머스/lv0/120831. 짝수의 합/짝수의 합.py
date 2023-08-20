def solution(n):
    answer = 0
    for i in range(n+1):
        if not i%2:
            answer+=i 
    return answer

def solution(n):
    return sum(i for i in range(n+1) if not i%2)