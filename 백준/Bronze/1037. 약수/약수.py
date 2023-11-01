n = int(input())
m = list(map(int,input().split()))
m.sort()
if n != 1:
    print(max(m)*min(m))
else:
    print(m[0]**2)