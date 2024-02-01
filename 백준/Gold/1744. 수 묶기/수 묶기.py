n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
ans = arr.count(1)

m = [i for i in arr if i<=0]
p = [i for i in arr if i>1]
p.sort()
m.sort(reverse=True)

while len(p)>=1:
    if len(p)>=2:
        a = p.pop()
        b = p.pop()
        ans+=a*b
    elif len(p)==1:
        a = p.pop()
        ans+=a
        
while len(m)>=1:
    if len(m)>=2:
        a = m.pop()
        b = m.pop()
        ans+=a*b
    elif len(m)==1:
        a = m.pop()
        ans+=a
        
print(ans)