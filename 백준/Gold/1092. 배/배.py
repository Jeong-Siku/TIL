n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
weights = sorted(list(map(int, input().split())), reverse=True)

cnt=0
if weights[0]>cranes[0]:
    print(-1)
else:
    while weights:
        for crane in cranes:
            if weights and crane<weights[-1]:
                continue
            for weight in weights:
                if crane>=weight:
                    weights.remove(weight)
                    break
        cnt+=1
    print(cnt)