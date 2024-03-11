from collections import deque

def bfs(x,y):
        visited[x][y] = 1
        q = deque([[x,y]]) # 이중 배열로 하기 위해서 [[]]으로 해야한다. []으로만 하면 flatten으로 된다.
        while q:
            cur_x, cur_y=q.popleft()
            for i in range(8):
                nx = cur_x+dx[i]
                ny = cur_y+dy[i]
                if not (0<=nx<h and 0<=ny<w):
                    continue
                elif visited[nx][ny]==0 and graph[nx][ny]==graph[cur_x][cur_y]: # 새로운 위치가 이전에 위치와 섬 또는 바다인지가 일치할 때
                    q.append([nx,ny])
                    visited[nx][ny]=1
                    
while True:
    w, h = map(int, input().split())
    if w==0 and h ==0:
        break
    
    graph = []
    visited = [[0]*w for _ in range(h)]
    for i in range(h):
        graph.append(list(map(int, input().split())))
    
    dx = [1,-1,0,0,1,-1,-1,1]
    dy = [0,0,1,-1,1,-1,1,-1]
    
                    
    # if graph[x][y] == 1 and visited[x][y]==0 섬이면서 이전에 방문한적이 없는 곳이면 갯수 세는 조건을 작성하는 것이 필요하다.
    ans = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==0:
                ans+=1
            bfs(i,j)

    print(ans)