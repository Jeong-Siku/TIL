from collections import deque
m,n = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

tomato_1 = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1:
            tomato_1.append((i,j))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque(tomato_1)

def bfs(q):
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx,ny = x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0:
                graph[nx][ny] = graph[x][y]+1
                q.append((nx,ny))
                
bfs(q)

result = 0
for row in graph:
    if 0 in row:
        print(-1)
        break
    result = max(result,max(row))
else:
    print(result-1)