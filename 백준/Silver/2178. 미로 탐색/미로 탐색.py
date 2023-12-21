from collections import deque
n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
    
visited = [[10**6]*m for _ in range(n)]
visited[0][0] = 1

dxy = [[1,0],[-1,0],[0,1],[0,-1]]
# 최단거리
q = deque()

def bfs(x,y):
    q.append((x,y))
    while q:
        cur_x,cur_y = q.popleft()
        for dx,dy in dxy:
            nx,ny = cur_x+dx,cur_y+dy
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==0 or visited[cur_x][cur_y]+1>=visited[nx][ny]:
                continue
            visited[nx][ny] = visited[cur_x][cur_y]+1
            q.append((nx,ny))
            
bfs(0,0)

print(visited[n-1][m-1])