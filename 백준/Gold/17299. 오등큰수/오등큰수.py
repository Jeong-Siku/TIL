from collections import deque
from collections import defaultdict

n = int(input())
arr = list(map(int,input().split()))

cnt = defaultdict(int) # 등장 횟수
for i in arr:
    cnt[i]+=1
    
result = [-1]*n
F = [cnt[i] for i in arr]

temp = deque()
for i in range(n):
    while temp and temp[-1][0]<F[i]:
        result[temp.pop()[1]]=arr[i]
    temp.append([F[i],i])
    
print(*result)