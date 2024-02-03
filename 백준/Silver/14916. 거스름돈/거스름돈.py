n = int(input())
ans = 0
if n==1 or n==3:
    ans = -1
elif n%5%2==0:
    ans+=n//5
    ans+=n%5//2
elif n%5%2==1:
    ans+=n//5-1
    ans+=(n%5+5)//2

print(ans)