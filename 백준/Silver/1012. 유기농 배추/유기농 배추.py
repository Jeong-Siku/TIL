from collections import deque
import sys
# 이동할 수 있다.
# 연결되어있으면 집단을 한번에 해결하여 특정 수로 바꾸는 게 좋을 듯?
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    m,n,k= map(int,input().split())
    matrix = [[0]*(m+2) for _ in range(n+2)]

    for _ in range(k):
        x,y=map(int,input().split())
        matrix[y+1][x+1]=1

    dirs = ((-1,0),(1,0),(0,-1),(0,1))
    move_q = deque()
    warm=0
    for i in range(1,m+2):
        for j in range(1,n+2):
            if matrix[j][i]==1:
                move_q.append([j,i])
                warm+=1
                while move_q:
                    cur_p = move_q.popleft()
                    if matrix[cur_p[0]][cur_p[1]] == 1:
                        matrix[cur_p[0]][cur_p[1]] = 0 
                        for x,y in dirs:
                            if matrix[cur_p[0]+x][cur_p[1]+y] == 1:
                                move_q.append([cur_p[0]+x,cur_p[1]+y])
    print(warm)