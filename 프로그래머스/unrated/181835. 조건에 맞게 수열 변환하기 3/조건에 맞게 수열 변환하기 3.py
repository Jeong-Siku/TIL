def solution(arr, k):
    answer = []
    if k%2:
        return [i*k for i in arr]
    else:
        return [i+k for i in arr]