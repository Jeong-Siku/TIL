import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
dp = [0]*(n)
dp[0]=arr[0]
if n>=2:
    dp[1]=arr[0]+arr[1]
if n>=3:
    dp[2]=max(dp[1],arr[0]+arr[2],arr[1]+arr[2])
for i in range(3,n):
    dp[i]=max(dp[i-1],dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i])
    
print(max(dp))