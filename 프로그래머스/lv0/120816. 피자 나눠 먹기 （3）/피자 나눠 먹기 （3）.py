def solution(slice, n):
    answer = 1
    while True:
        if slice*answer//n >= 1:
            return answer
        answer+=1
    