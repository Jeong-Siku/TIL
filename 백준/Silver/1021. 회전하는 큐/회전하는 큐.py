from collections import deque
n, m = map(int,input().split())
arr = deque([i+1 for i in range(n)])
finds = list(map(int,input().split()))

cnt=0
for find in finds:
    while True:
        if arr[0] == find:
            arr.popleft()
            break
        if arr.index(find)>= len(arr)/2:
            arr.appendleft(arr.pop())
            cnt+=1
        else:
            arr.append(arr.popleft())
            cnt+=1

print(cnt)