import sys
input = sys.stdin.readline

n = int(input())
graph = [0]
for _ in range(n):
    graph.append(int(input()))
    
dp = [0]*(n+1)
dp[1] = graph[1]

for i in range(2,n+1):
    if i==2:
        dp[2] = graph[2]+graph[1]
    if i>2:
        dp[i] = max(dp[i-2]+graph[i],dp[i-3]+graph[i-1]+graph[i])

print(dp[-1])