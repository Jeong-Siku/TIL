n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
b.sort(reverse=True)
result = 0
for i,j in zip(a,b):
    result+=i*j

print(result)