n, k = map(int, input().split())
from collections import deque
def bfs(n,v):
    cnt=0
    q = deque([n])
    v[n]=1
    if n==k:
        return cnt
    while q: 
        for _ in range(len(q)): # cnt+=1이 되는 순간이 하나의 노드가 지날 때가 아닌 각 자식노드를 한번씩 둘러봤을 때이므로 for문을 배치한다.
            x = q.popleft()
            for i in [1, -1, x]:
                dx = x+i
                if 0<=dx<=100000 and v[dx]!=1:
                    if dx==k:
                        return cnt+1
                    else:
                        v[dx] = 1
                        q.append(dx)
        cnt+=1

v = [0]*100001
print(bfs(n,v))