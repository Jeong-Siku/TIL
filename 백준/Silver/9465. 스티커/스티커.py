t = int(input())
for _ in range(t):
    n = int(input())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    dp1 = [0]*n
    dp1[0] = arr1[0]
    dp2 = [0]*n
    dp2[0] = arr2[0]
    if n>=2:
        dp1[1] = arr1[1]+arr2[0]
        dp2[1] = arr2[1]+arr1[0]
        for i in range(2,n):
            dp1[i],dp2[i] = max(dp1[i-2]+arr1[i],dp2[i-2]+arr1[i],dp2[i-1]+arr1[i]), max(dp2[i-2]+arr2[i],dp1[i-2]+arr2[i],dp1[i-1]+arr2[i])
        print(max(dp1[-1],dp2[-1]))
    else:
        print(max(dp1[0],dp2[0]))
        