def solution(sides):
    answer = 0
    return (max(sides)>=(sum(sides)-max(sides)))+1