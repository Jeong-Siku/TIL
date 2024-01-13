n = int(input())
arr = [0]+list(map(int,input().split()))

dp = [0]*(n+1)
dp[1] = arr[1]
for i in range(2,n+1):
    dp[i] = max([dp[j]+arr[i-j] for j in range(i)])

print(dp[n])