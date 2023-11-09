t = int(input())
arr = [0 for _ in range(11)]
arr[0:4] = [1,1,2,4,7]

for i in range(5,11):
    arr[i] = arr[i-3]+arr[i-2]+arr[i-1]
    
for _ in range(t):
    n = int(input())
    print(arr[n])