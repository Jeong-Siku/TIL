def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        else:
            continue
    
    if len(answer)>k:
        while len(answer) != k:
            answer.pop()
    elif len(answer)<k:
        while len(answer) != k:
            answer.append(-1)

    return answer

def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            answer.append(i)
        if len(answer) ==k:
            break
    return answer+[-1]*(k-len(answer))