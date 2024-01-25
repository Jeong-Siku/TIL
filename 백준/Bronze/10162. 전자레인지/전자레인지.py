t = int(input())
times = [300,60,10]
result = []
for i in times:
    result.append(t//i)
    t%=i
if t:
    print(-1)
else:
    print(*result)