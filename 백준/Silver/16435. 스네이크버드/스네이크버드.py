n, l = map(int, input().split())
leng = sorted(list(map(int, input().split())))+[100002]

while True:
    if l >= leng[0]:
        leng.pop(0)
        l+=1
    else:
        break

print(l)