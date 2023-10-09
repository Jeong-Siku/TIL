from collections import Counter
n = int(input())
check = list(map(int,input().split()))
m = int(input())
need_check = list(map(int,input().split()))
count = Counter(check)
for i in need_check:
    print(count[i],end=" ")