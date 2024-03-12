from collections import deque
t = int(input())

dx = [2,2,-2,-2,1,1,-1,-1]
dy = [1,-1,1,-1,2,-2,2,-2]

def bfs(x,y):
    visited[x][y]=0
    q = deque([[x,y]])
    while q:
        cur_x, cur_y = q.popleft()
        if cur_x==goal_x and cur_y==goal_y:
            break
        for i in range(8):
            nx=cur_x+dx[i]
            ny=cur_y+dy[i]
            if not (0<=nx<n and 0<=ny<n):
                continue
            elif visited[nx][ny]==0 :
                visited[nx][ny]=visited[cur_x][cur_y]+1
                q.append([nx,ny])

for _ in range(t):
    n = int(input())
    loc_x, loc_y = map(int, input().split())
    goal_x, goal_y = map(int, input().split())
    visited = [[0]*n for _ in range(n)]
    bfs(loc_x, loc_y)
    print(visited[goal_x][goal_y])