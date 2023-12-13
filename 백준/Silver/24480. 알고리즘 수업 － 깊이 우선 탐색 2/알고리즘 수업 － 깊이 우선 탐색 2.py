import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0]*(n+1)
order = [0]*(n+1)
cnt = 1
def dfs(graph,visited,r):
    global cnt
    visited[r]=1
    order[r]=cnt
    graph[r].sort(reverse=True)
    for i in graph[r]:
        if not visited[i]:
            cnt+=1
            dfs(graph,visited,i)

dfs(graph,visited,r)

print(*order[1:])