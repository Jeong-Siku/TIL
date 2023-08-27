def solution(num, k):
    return int(str(num).find(str(k)))+1 if int(str(num).find(str(k)))+1 else -1