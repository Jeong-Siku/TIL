n = int(input())
have = list(map(int,input().split()))
m = int(input())
check = list(map(int,input().split()))

dp = {}
for i in have:
    dp[i]=1

for i in check:
    if dp.get(i,0):
        print(1,end=" ")
    else:
        print(0,end=" ")