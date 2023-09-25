from collections import deque
def solution(prices):
    q = deque(prices)
    result = []
    while q:
        cur = q.popleft()
        sec = 0
        for i in q:
            if cur <= i:
                sec+=1
            else:
                sec+=1
                break
        result.append(sec)
    return result