def solution(order):
    answer = 0
    for i in str(order):
        if i in "369":
            answer+=1
    return answer

def solution(order):
    return sum(map(lambda x:str(order).count(x),["3","6","9"]))