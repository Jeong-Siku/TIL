import heapq
n, m = map(int, input().split())
arr = sorted(list(map(int,input().split()))) 

for _ in range(m):
    sum_min = heapq.heappop(arr)+heapq.heappop(arr)
    heapq.heappush(arr, sum_min)
    heapq.heappush(arr, sum_min)

print(sum(arr))