n, k = map(int, input().split())
nations = []
for _ in range(n):
    c, g, s, b = map(int, input().split())
    nations.append([c,g,s,b])
nations.sort(key=lambda x: (-x[1],-x[2],-x[3],x[0]))

rnk = 1
nations[0]+=[1]
for i in range(1,n):
    if nations[i][1:] == nations[i-1][1:4]:
        nations[i]+=[rnk]
    else:
        rnk+=1
        nations[i]+=[rnk]

print(nations[k-1][4])