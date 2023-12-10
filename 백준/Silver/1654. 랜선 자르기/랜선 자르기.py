import sys
input = sys.stdin.readline

k,n = map(int,input().split())

arr = []

for _ in range(k):
    arr.append(int(input()))

start = 1
end = max(arr) 
result = 0

while start<=end:
    cnt = 0
    mid = (start+end)//2
    for i in arr:
        cnt+=i//mid
    if n > cnt:
        end = mid-1
    else:
        result=mid
        start = mid+1
print(result)