n = int(input())

alp = []
for _ in range(n):
    a = input()
    if a not in alp:
        alp.append(a)
        
alp.sort(key = lambda x:(len(x),x))

for i in alp:
    print(i)