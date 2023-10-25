n = int(input())
result = []
for i in range(1,n+1):
    if n == sum([int(i) for i in str(i)])+i:
        result.append(i)
        break
if result:
    print(*result)
else:
    print(0)

