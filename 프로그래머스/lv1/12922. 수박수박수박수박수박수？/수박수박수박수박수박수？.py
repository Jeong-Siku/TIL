def solution(n):
    answer = ''
    for i in range(n):
        if not i%2:
            answer+="수"
        else:
            answer+="박"
    return answer

def solution(n):
    return "".join("박" if i%2 else "수" for i in range(n))

def solution(n):
    return "수박"*(n//2) + "수"*(n%2)