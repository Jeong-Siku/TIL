n = int(input())
arr = [0 for _ in range(n+1)]
arr[2:6]=[1,1,2,3]

for i in range(6, n+1):
    if i%2==0 and i%3==0:
        arr[i] = min(arr[i//2]+1,arr[i//3]+1,arr[i-1]+1)
    elif i%2==0:
        arr[i] = min(arr[i//2]+1,arr[i-1]+1)
    elif i%3==0:
        arr[i] = min(arr[i//3]+1,arr[i-1]+1)
    else:
        arr[i] = arr[i-1]+1

print(arr[n])