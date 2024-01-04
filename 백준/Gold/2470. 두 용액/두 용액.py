n = int(input())
arr = list(map(int,input().split()))

arr.sort()
start,end = 0,n-1
min_gap = float('inf')
result = []

while start<end :
    sum_two = arr[start]+arr[end]
    if abs(sum_two)<=abs(min_gap):
        min_gap = min(abs(sum_two),abs(min_gap))
        result.append([arr[start],arr[end]])
    if sum_two<0:
        start+=1
    elif sum_two>0:
        end-=1
    else:
        start+=1
        end-=1
    
print(*result[-1])