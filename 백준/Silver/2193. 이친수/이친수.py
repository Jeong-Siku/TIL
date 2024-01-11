n = int(input())

dp = [0]*(n+1)
dp[1]=(0,1)
if n>1:
    dp[2]=(1,0)

for i in range(3,n+1):
    dp[i] = (dp[i-1][0]+dp[i-1][1],dp[i-1][0])
    
print(sum(dp[n]))