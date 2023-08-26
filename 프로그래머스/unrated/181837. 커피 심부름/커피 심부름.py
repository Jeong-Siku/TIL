def solution(order):
    answer = sum([5000 if "latte" in i else 4500 for i in order])
    return answer