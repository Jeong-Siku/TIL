import heapq
def solution(operations):
    answer = []
    q = []
    for i in operations:
        sig, num = i.split()
        if sig =="I":
            heapq.heappush(q,int(num))
            
        elif q and sig == "D" and num == "1":
            q = list(map(lambda x: x*(-1),q))
            q.sort()
            heapq.heappop(q)
            q = list(map(lambda x: x*(-1),q))
            q.sort()
        elif q and sig == "D" and num == "-1":
            heapq.heappop(q)
    if q:
        return max(q),min(q)
    return 0,0