def solution(array, height):
    answer = 0
    for i in array:
        if i>height:
            answer+=1
    return answer

def solution(array, height):
    return sum(1 for i in array if i>height)