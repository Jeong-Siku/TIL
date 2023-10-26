a, b, c, d, e, f = list(map(int,input().split()))
result = []
for i in range(-999,1000):
    for j in range(-999,1000):
        if a*i+b*j==c and d*i+e*j==f:
            result=[i,j]
            break
print(*result)