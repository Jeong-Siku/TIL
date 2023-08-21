def solution(hp):
    answer = 0
    ants = [5,3,1]
    cur = hp
    for i in ants:
        answer+=cur//i
        cur = cur%i
    return answer