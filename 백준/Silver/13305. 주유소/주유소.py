import sys
input = sys.stdin.readline
n = int(input().rstrip())
len_road = list(map(int,input().rstrip().split()))
price = list(map(int,input().rstrip().split()))[:-1]

min_price = min(price)

total_price = 0
for i in range(n-1):
    if price[i] == min_price:
        total_price += price[i]*sum(len_road[i:])
        break
    if price[i]<price[i+1]:
        price[i+1]=price[i]
    
    total_price += price[i]*len_road[i]

print(total_price)