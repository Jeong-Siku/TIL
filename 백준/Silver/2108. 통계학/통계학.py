from collections import defaultdict
import sys
n = int(input())
input = sys.stdin.readline

dic = defaultdict(int)

arr = []
for _ in range(n):
    num = int(input().rstrip())
    dic[num]+=1
    arr.append(num)
    
max_cnt = max(dic.values())
fre_cnt = [k for k,v in dic.items() if v == max_cnt]

arr.sort()
fre_cnt.sort()

print(round(sum(arr)/len(arr)))
print(arr[int(len(arr)/2)])
print(fre_cnt[1] if len(fre_cnt)>1 else fre_cnt[0])
print(max(arr)-min(arr))