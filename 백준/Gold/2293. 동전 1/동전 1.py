import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
arr.sort()

dp = [0]*(k+1)
dp[0] = 1
for j in arr:
    for i in range(j,k+1):  
        dp[i]+=dp[i-j]
        
print(dp[k])