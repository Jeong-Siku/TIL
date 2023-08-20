def solution(arr):
    idx = []
    for i in range(len(arr)):
        if arr[i]==2:
            idx.append(i)
    if idx:
        answer = arr[idx[0]:idx[-1]+1]
    else:
        answer = [-1]
    return answer