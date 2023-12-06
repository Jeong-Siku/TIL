from collections import deque
import sys
input = sys.stdin.readline

n,m,r = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

visited = [0]*(n+1)
order = [0]*(n+1)
t = 1

def bfs(graph,visited,r):
    global t
    global order
    q=deque([r])
    visited[r]=1
    order[r]=t
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] == 0:
                visited[i]=1
                q.append(i)
                t+=1
                order[i]=t

bfs(graph,visited,r)

for i in order[1:]:
    print(i)