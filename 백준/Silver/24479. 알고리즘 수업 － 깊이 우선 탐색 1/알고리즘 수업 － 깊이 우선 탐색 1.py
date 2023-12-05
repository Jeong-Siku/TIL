import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n,m,r = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

graph = [sorted(i) for i in graph]

visited = [False]*(n+1)
visit_num = [0]*(n+1)
t = 1 # 각 노드에서 되돌아 갔을 때도 숫자를 유지해야한다.
def dfs(visited,graph,r):
    global t
    visited[r]=True
    visit_num[r]=t
    for i in graph[r]:
        if visited[i]==False:
            t+=1
            dfs(visited,graph,i)

dfs(visited,graph,r)

for i in visit_num[1:]:
    print(i)