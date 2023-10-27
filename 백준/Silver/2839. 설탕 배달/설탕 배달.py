n = int(input())

result = []
for i in range(n//5,-1,-1):
    for j in range(n//3+1):
        if 5*i+3*j==n:
            result.append(i+j)
            break
if result:
    print(min(result))
else:
    print(-1)
        