a, b = map(int,input().split())

cnt = 1
while b >= 1:
    if b < a:
        print(-1)
        break
    elif b==a:
        print(cnt)
        break
    if b%2==0 :
        b//=2
        cnt+=1
    elif str(b)[-1]=='1' :
        b=int(str(b)[:-1])
        cnt+=1
    else:
        print(-1)
        break