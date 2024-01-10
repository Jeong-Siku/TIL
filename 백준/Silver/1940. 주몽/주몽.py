n =int(input())
m = int(input())
arr = list(map(int,input().split()))
arr.sort()

start,end=0,n-1
cnt=0
while start<end:
    sum_two = arr[start]+arr[end]
    if sum_two==m:
        cnt+=1
        start+=1
        end-=1
    elif sum_two<m:
        start+=1
    elif sum_two>m:
        end-=1
print(cnt)