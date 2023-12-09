n = int(input())
arr = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))

arr.sort()

def binary_search(arr,target,start,end): 
    while start<=end:
        mid = (start+end)//2
        if arr[mid]==target:
            return 1
        elif arr[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return 0

for target in find:
    print(binary_search(arr,target,0,n-1))