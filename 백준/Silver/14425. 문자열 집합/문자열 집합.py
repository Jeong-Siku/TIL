n,m = list(map(int,input().split()))
check = []
for _ in range(n):
    check.append(input())
checking = []
for _ in range(m):
    checking.append(input())
result= 0
for i in checking:
    if i in check:
        result+=1
print(result)