n = int(input())
s_len = int(input())
s = input()
pn = 'I'+'OI'*n

ans = 0
while pn in s:
    change = 'I'+'OI'*(n-1)
    s = s.replace(pn,change,1)
    ans+=1

print(ans)