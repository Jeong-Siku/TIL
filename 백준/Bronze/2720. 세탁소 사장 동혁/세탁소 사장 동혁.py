t = int(input())
for _ in range(t):
    change = int(input())
    num = []
    for coin in (25,10,5,1):
        num.append(change//coin)
        change = change%coin
    print(*num)