n = int(input())

arr = []
for _ in range(n):
    kg,cm = map(int,input().split())
    arr.append((kg,cm))
    
ranks = []
for i in range(n):
    rank = 0
    for j in range(n):
        if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
            rank+=1
    ranks.append(rank+1)

print(*ranks)