n = sorted(list(map(int,list(input()))), reverse=True)

if sum(n)%3 != 0 or 0 not in n:
    print(-1)
else:
    for i in n:
        print(i, end='')