from collections import deque
n = int(input())
arr = list(map(int,input().split()))

result = [-1]*n

A = deque()
for i in range(n):
    while A and A[-1][0]<arr[i]:
        result[A.pop()[1]] = arr[i]
    A.append([arr[i],i])
print(*result)