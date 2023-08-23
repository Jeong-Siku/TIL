def solution(arr, flag):
    answer = []
    for a,b in zip(arr,flag):
        if b:
            for i in range(a*2):
                answer.append(a)
        else:
            for i in range(a):
                answer.pop()
    return answer