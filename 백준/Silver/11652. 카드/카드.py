n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))
nums.sort()

from collections import defaultdict
dic = defaultdict(int)
for i in nums:
    dic[i]+=1
    
sorted_dic = sorted(dic.items(),key=lambda x: (-x[1],x[0]))
print(sorted_dic[0][0])