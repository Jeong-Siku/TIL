def solution(arr):
    answer = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            answer.append(arr[i][j]==arr[j][i])
    return int(all(answer))

def solution(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1