import sys
input = sys.stdin.readline
n,k = map(int,input().rstrip().split())
arr = list(map(int,input().rstrip().split()))
tem = sum(arr[0:k])
max_tem = tem

for i in range(1,n-k+1):
    tem = tem-arr[i-1]+arr[i+k-1]
    if tem>max_tem:
        max_tem = tem
        
print(max_tem)