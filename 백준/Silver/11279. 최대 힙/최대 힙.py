import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())

heap = []

for _ in range(n):
    num = int(input().rstrip())
    heapq.heappush(heap,(-num,num))
    if not num:
        print(heap[0][1])
        heapq.heappop(heap)