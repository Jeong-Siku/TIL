import sys
import heapq
input = sys.stdin.readline
n = int(input())

left = []
right = []
called = []

for _ in range(n):
    called.append(int(input()))
mid = called[0] # 처음값은 중간값이 된다.
result = [mid] 

for i in range(1,n):
    if called[i]>=mid:
        heapq.heappush(right,called[i])
    else:
        heapq.heappush(left,-called[i])
    if (i+1)%2==0: # i+1은 총 원소의 개수
        if len(left) > len(right):
            heapq.heappush(right,mid) # 짝수개의 원소개에서 중간값 중 최소값이 mid가 되기 때문에 최소값보다 큰 이전의 mid는 right로 이동
            mid = -heapq.heappop(left)
    else:
        if len(left)+2 == len(right):
            heapq.heappush(left,-mid)
            mid= heapq.heappop(right)
    result.append(mid)
for i in result:
    print(i)