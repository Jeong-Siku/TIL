for _ in range(int(input())):
    n, m = list(map(int,input().split()))
    a = 1
    b = 1
    for i in range(m-n+1,m+1):
        a*=i
    for i in range(1,n+1):
        b*=i
    print(int(a/b))