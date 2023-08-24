def solution(array, n):
    result = []
    array.sort()
    for idx,i in enumerate(array):
        result.append([idx,abs(i-n)])
    result.sort(key=lambda x : (x[1],x[0]))
    return array[result[0][0]]