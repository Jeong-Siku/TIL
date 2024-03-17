n = int(input())
arrs = []
for _ in range(n):
    arr = list(input())
    sum_arr = 0
    for i in arr:
        if i.isdigit():
            sum_arr+=int(i)
    arrs.append([arr,sum_arr])

arrs.sort(key=lambda x : (len(x[0]),x[1],"".join(x[0])))
for i in [''.join(i[0]) for i in arrs]:
    print(i)