def solution(arr):
    answer = []
    for i in arr:
        if not answer:
            answer+=[i]
        elif answer and answer[-1]==i:
            answer.pop()
        else:
            answer+=[i]
            
    
    return answer if answer else [-1]