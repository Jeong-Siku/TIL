name = list(input())

pre = []
odd = 0
odd_alp = []
for i in sorted(set(name)):
    if name.count(i)%2==1:
        odd+=1
        odd_alp.append(i)
    pre.append(i*(name.count(i)//2))
    
if odd>1 :
    print("I'm Sorry Hansoo")
else:
    print(''.join(pre+odd_alp+sorted(pre,reverse=True)))