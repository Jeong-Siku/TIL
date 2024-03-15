import sys
input = sys.stdin.readline
t = int(input().rstrip())
        
for _ in range(t):
    n = int(input().rstrip())
    arr = []
    for _ in range(n):
        arr.append(input().rstrip())
    arr.sort()
    
    for i in range(n-1):
        if arr[i] == arr[i+1][:len(arr[i])]:
            print('NO')
            break
    else:
        print('YES')

