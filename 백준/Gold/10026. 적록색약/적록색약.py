import sys
sys.setrecursionlimit(10 ** 6)

def dfs(x,y,visited,matrix):
    visited[x][y]=1
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n:
            continue
        if visited[nx][ny]==0 and matrix[x][y] == matrix[nx][ny]: # matrix조건으로 동일한 색상인지 판단하는 것이 필요
            dfs(nx,ny,visited,matrix)

n = int(input())
# 적록색약 X
matrix = [input() for _ in range(n)] # matrix의 변경이 필요없다면 List로 작성할 필요는 없다
visited = [[0]*n for _ in range(n)]
# 적록색약 o
matrix_o = [i.replace('G','R') for i in matrix]
visited_o = [[0]*n for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ans = 0
ans_o = 0
for i in range(n):
    for j in range(n):
        if visited[i][j]==0:
            dfs(i,j,visited,matrix)
            ans+=1
        if visited_o[i][j]==0:
            dfs(i,j,visited_o,matrix_o)
            ans_o+=1
print(ans, ans_o)