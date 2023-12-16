n = int(input())
graph = [[0]*(n+1)]
for _ in range(n):
    graph.append([0]+list(map(int,list(input()))))

visited = [[0]*(n+1) for _ in range(n+1)]
dongs = [[0]*(n+1) for _ in range(n+1)] # 동의 숫자를 입력하는 배열
dong_num = 1

def dfs(x,y,dong_num):
    if x<1 or x>n or y<1 or y>n:
        return False
    if graph[x][y]==1 and visited[x][y]==False:
        visited[x][y]=True
        dongs[x][y]=dong_num
        dfs(x-1,y,dong_num)
        dfs(x+1,y,dong_num)
        dfs(x,y-1,dong_num)
        dfs(x,y+1,dong_num)
        return True
    return False

for i in range(1,n+1):
    for j in range(1,n+1):
        if dfs(i,j,dong_num) == True: # 새로운 동에 입장했을 때만 적용된다.
            dong_num+=1
            
from collections import defaultdict

dong_cnt = defaultdict(int)
for i in range(1,n+1):
    for j in range(1,n+1):
        dong_cnt[dongs[i][j]]+=1

if 0 in dong_cnt.keys():
    del dong_cnt[0]
print(len(list(dong_cnt)))
for i in sorted(list(dong_cnt.values())):
    print(i)