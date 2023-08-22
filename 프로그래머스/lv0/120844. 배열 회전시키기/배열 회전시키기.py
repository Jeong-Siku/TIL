def solution(numbers, direction):
    answer=[]
    if direction=="right":
        # 하나의 값은 리스트가 아니기에 병합할 수 없음.
        # 리스트화 필요
        return [numbers[-1]]+numbers[:-1]
    else:
        return numbers[1:]+[numbers[0]]
    
from collections import deque

def solution(numbers, direction):
    numbers = deque(numbers)
    if direction=="right":
        numbers.rotate(1)
    else:
        numbers.rotate(-1)
    return list(numbers)
