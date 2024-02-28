s = input()
ans = ''
for alp in s:
    if alp.isupper():
        ans+=alp.lower()
    else:
        ans+=alp.upper()
print(ans)