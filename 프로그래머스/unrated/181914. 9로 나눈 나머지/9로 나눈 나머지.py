def solution(number):
    answer = 0
    for i in number:
        answer+=int(i)
    return answer%9

def solution(number):
    return sum(list(map(int,number)))%9