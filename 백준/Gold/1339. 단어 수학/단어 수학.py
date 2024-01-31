from collections import defaultdict
n = int(input())
dics = []
for _ in range(n):
    dics.append(input())

result = defaultdict(int)
for dic in dics:
    for idx in range(len(dic)):
        result[dic[idx]] += 10**(len(dic)-idx-1)

sum_value=0
sorted_result = sorted(result.items(),key=lambda x: x[1], reverse=True)
orders = [i for i in range(9,9-len(result),-1)]
for order,alp in enumerate(sorted_result):
    sum_value += alp[1]*orders[order]
print(sum_value)