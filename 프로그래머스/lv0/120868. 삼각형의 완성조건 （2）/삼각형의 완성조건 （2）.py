def solution(sides):
    answer = 0
    for i in range(1,sum(sides)):
        side=sides+[i]
        answer+=max(side)< (sum(side)-max(side))
    return answer