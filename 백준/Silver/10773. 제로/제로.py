k = int(input())
sum_arr = []
for _ in range(k):
    num = int(input())
    if num:
        sum_arr.append(num)
    else:
        sum_arr.pop()

print(sum(sum_arr))