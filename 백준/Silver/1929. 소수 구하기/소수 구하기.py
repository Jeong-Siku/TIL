m, n = map(int,input().split())
for i in range(m,n+1):
    for j in range(2,int(i**0.5)+1):
        if i%j==0:
            break
    else:
        if i != 1:
            print(i)