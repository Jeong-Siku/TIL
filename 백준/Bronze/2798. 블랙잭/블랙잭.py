from itertools import combinations
n,m = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr.sort()
result = []
for i in combinations(arr,3):
    if sum(i) <=m :
        result.append(sum(i))
print(max(result))