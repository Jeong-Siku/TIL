def solution(a, b):
    answer = 0
    a,b = min(a,b), max(a,b)
    for i in range(a,b+1):
        answer+=i
    return answer

def solution(a, b):
    a,b = min(a,b), max(a,b)
    return sum(range(a,b+1))