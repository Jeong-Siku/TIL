n, k = map(int,input().split())

g = 0

for i in range(min(n,k),0,-1):
    if n%i==0 and k%i==0:
        g = i
        print(g)
        break

if g:
    l = g*(n//g)*(k//g)
    print(l)
else:
    print(0)