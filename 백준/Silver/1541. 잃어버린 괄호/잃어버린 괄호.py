arr = input()

split_arr = arr.split("-")

sum_arr = [sum(map(int,i.split("+"))) for i in split_arr]

result = sum_arr[0]
for idx,i in enumerate(sum_arr):
    if idx:
        result-=i
print(result)