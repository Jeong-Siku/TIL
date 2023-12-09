import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dp = [[float("inf")]*3 for _ in range(n)]
dp[0] = graph[0]
for i in range(1,n):
    for j in range(3):
        for k in range(3):
            if j==k:
                continue
            else:
                dp[i][j] = min(graph[i][j]+dp[i-1][k],dp[i][j])
                
print(min(dp[n-1]))