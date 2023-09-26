from collections import Counter
a = input().lower()

count = Counter(a)

dic = dict(count)

max_cnt = max(dic.values())

result = [i for i in dic if dic[i] == max_cnt]
        
print("?") if len(result)>=2 else print(result[0].upper())