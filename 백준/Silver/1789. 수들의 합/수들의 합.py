s = int(input())

result = 0
n = []
num=1
while result <= s:
    result+=num
    n.append(num)
    num+=1
if result-s in n:
    print(len(n)-1)
else:
    print(len(n)-1)