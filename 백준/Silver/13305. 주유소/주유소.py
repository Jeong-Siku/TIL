import sys
input = sys.stdin.readline
n = int(input().rstrip())
len_road = list(map(int,input().rstrip().split()))
price = list(map(int,input().rstrip().split()))
# 가장 가격이 낮은 도시에서 남은 거리의 기름을 다 산다.
min_price = sorted(price)[1]

total_price = 0
total_len = sum(len_road)
for i in range(len(len_road)):
    if price[i] != min_price:
        total_price += price[i]*len_road[i]
        total_len -= len_road[i]
    else:
        total_price += price[i]*total_len
        break
    
print(total_price)