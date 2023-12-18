n = int(input())
indexs = []
for _ in range(n):
    indexs.append(list(map(int,input().split())))

indexs.sort(key = lambda x:(x[1],x[0]))

for index in indexs:
    print(*index)