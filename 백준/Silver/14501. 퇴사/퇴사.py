n = int(input())
t = []
p = []
for _ in range(n):
    time, price = map(int,input().split())
    t.append(time)
    p.append(price)
    
dp = [0]*(n+1)
for i in range(n):
    for j in range(i+t[i],n+1):
        if dp[i]+p[i]> dp[j]:
            dp[j]=dp[i]+p[i]
            
print(dp[-1])