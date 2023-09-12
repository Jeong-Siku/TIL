def solution(arr):
    # 가장 작은 수를 제거
    if len(arr) ==1:
        return [-1]
    else:
        min_arr = min(arr)
        del arr[arr.index(min_arr)]
        return arr