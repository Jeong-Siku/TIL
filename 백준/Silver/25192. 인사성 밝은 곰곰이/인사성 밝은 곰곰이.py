n = int(input())
arr = set()
cnt=0
for _ in range(n):
    mes = input()
    if mes == "ENTER":
        cnt += len(arr)
        arr = set()
        continue
    else:
        arr.add(mes)
cnt+=len(arr)

print(cnt)