from math import *
n, m = map(int,input().split())
if n>=3 and 7<=m:
    cnt=4+m-6
elif n>=3 and m<=4:
    cnt=m
elif n>=3 and 5<=m<=6:
    cnt=4
elif n==2:
    if m<=8:
        cnt=ceil(m/2)
    else:
        cnt=4
elif n==1:
    cnt=1

print(cnt)