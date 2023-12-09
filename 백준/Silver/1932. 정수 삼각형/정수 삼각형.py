import sys
input = sys.stdin.readline
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
dp = [[0]*i for i in range(1,n+1)]
dp[0] = graph[0]

for i in range(1,n):
    for k in range(len(graph[i])):
        for j in range(len(graph[i-1])):
            if k==j or k-1 == j:
                dp[i][k] = max(dp[i-1][j]+graph[i][k],dp[i][k])
print(max(dp[n-1]))