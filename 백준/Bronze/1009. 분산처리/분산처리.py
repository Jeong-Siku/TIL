import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    cnt = 1
    num = [a%10]
    first = a
    while cnt!=b:
        cnt+=1
        if a*first%10 not in num:
            num.append(a*first%10)
            a=a*first%10
        else:
            break
    print(10 if num[b%len(num)-1] ==0 else num[b%len(num)-1])