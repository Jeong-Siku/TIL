n = int(input())
dan_arr = ["ChongChong"]
for _ in range(n):
    a, b = input().split()
    if a in dan_arr:
        dan_arr.append(b)
    elif b in dan_arr:
        dan_arr.append(a)
print(len(set(dan_arr)))