def solution(arr, divisor):
    answer = sorted(i for i in arr if not i%divisor)
    return answer if answer else [-1]