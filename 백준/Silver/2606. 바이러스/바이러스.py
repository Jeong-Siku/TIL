com_cnt = int(input())
node_cnt = int(input())

graph = [[] for _ in range(com_cnt+1)]
for _ in range(node_cnt):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [0]*(com_cnt+1)
cnt = 0
def dfs(graph,visited,s):
    global cnt
    cnt+=1
    visited[s]=cnt
    for i in graph[s]:
        if visited[i]==0:
            dfs(graph,visited,i)

dfs(graph,visited,1)

print(cnt-1)