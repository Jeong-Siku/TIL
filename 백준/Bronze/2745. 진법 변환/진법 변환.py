n,b = input().split()

b=int(b)
num = 0
for idx,i in enumerate(n[::-1]):
    if i.isalpha():
        num+=(ord(i)-ord("A")+10)*(b**idx)
    else:
        num+=int(i)*(b**idx)
print(num)