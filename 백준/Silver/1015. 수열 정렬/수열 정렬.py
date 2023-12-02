n = int(input())
a = list(map(int,input().split()))
p = [i for i in range(n)]

sorted_a = sorted(a)

from collections import defaultdict
dic = defaultdict(int)
for i in sorted_a:
        dic[i]=sorted_a.index(i)
        
arr = []
for i in a:
    if dic[i] not in arr:
        arr.append(dic[i])
    else:
        dic[i]+=1
        arr.append(dic[i])
        
print(*arr)