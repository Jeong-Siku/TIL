n = int(input())
arr = list(map(int,input().split()))
x = int(input())

arr.sort()

cnt=0
start,end=0,n-1
while start<end:
    sum_ = arr[start]+arr[end]
    if sum_>x:
        end-=1
    elif sum_<x:
        start+=1
    else:
        cnt+=1
        start+=1
        end-=1
print(cnt)