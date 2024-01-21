from collections import deque
n, k = map(int,input().split())
arr = deque([i for i in range(1,n+1)])

result = []
for i in range(n):
    arr.rotate(-(k-1))
    result.append(arr.popleft())
print('<{}>'.format(', '.join(map(str,result))))
    