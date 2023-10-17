n = int(input())
m = int(input())
sum_arr = []
for i in range(n,m+1):
    if i==1:
        continue
    for j in range(2,i):
        if i%j == 0 :
            break
    else:
        sum_arr.append(i)
if sum_arr:
    print(sum(sum_arr))
    print(min(sum_arr))
else:
    print(-1)