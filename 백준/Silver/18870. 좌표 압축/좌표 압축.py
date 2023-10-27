from collections import defaultdict
n = int(input())
arr = list(map(int,input().split()))

mod_arr = sorted(list(set(arr)))

dic = defaultdict()

for mod,i in zip(mod_arr,range(len(arr))):
    if mod in dic.keys():
        pass
    else:
        dic[mod]=i

result = []
for i in arr:
    result.append(dic[i])

print(*result)
