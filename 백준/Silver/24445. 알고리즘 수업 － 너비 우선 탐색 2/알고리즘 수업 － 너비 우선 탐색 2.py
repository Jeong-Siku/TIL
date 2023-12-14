from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0]*(n+1)
order = [0]*(n+1)
cnt = 1
q = deque()
def bfs(graph,visited,r):
    global cnt
    visited[r]=1
    order[r] = cnt
    q.append(r)
    while q:
        cur = q.popleft()
        graph[cur].sort(reverse=True)
        for i in graph[cur]:
            if not visited[i]:
                q.append(i)
                visited[i]=1
                cnt+=1
                order[i]=cnt
                
bfs(graph,visited,r)

for i in order[1:]:
    print(i)