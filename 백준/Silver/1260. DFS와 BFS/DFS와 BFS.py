from collections import deque
n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
q = deque()
dfs_order = deque()
dfs_order.append(r)
def dfs(graph,visited,r):
    visited[r] = True
    graph[r].sort()
    for i in graph[r]:
        if visited[i]==False:
            visited[i]=True
            dfs_order.append(i)
            dfs(graph,visited,i)

bfs_order = deque()
def bfs(graph,visited,r):
    visited[r] = True
    q.append(r)
    bfs_order.append(r)
    while q:
        cur = q.popleft()
        graph[cur].sort()
        for i in graph[cur]:
            if visited[i]==False:
                bfs_order.append(i)
                visited[i]=True
                q.append(i)
                
visited1 = [False]*(n+1) 
dfs(graph,visited1,r)
visited2=[False]*(n+1)
bfs(graph,visited2,r)
print(*list(dfs_order))
print(*list(bfs_order))