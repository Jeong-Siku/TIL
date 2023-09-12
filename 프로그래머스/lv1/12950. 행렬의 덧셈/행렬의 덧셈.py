def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr = []
        for j in range(len(arr1[0])):
            arr.append(arr1[i][j]+arr2[i][j])
        answer.append(arr)
    return answer

def solution(arr1, arr2):
    return [[c+d for c,d in zip(a,b)] for a,b in zip(arr1,arr2)]

def solution(arr1, arr2):
    return [list(map(sum,zip(*x))) for x in zip(arr1,arr2)]